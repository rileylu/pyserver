import nanomsg as nn
import traceback
from multiprocessing import cpu_count
import threading


class PyWorker:
    def __init__(self, worker_id):
        self._id = worker_id
        self._threads = []
        try:
            for i in range(cpu_count()):
                name = "[%s][thread%d]" % (self._id, i)
                self._threads.append(threading.Thread(target=WorkerRunner(name, "tcp://localhost:5557").run))
        except Exception:
            traceback.print_exc()
            raise

    def run(self):
        for t in self._threads:
            t.start()
        for t in self._threads:
            t.join()


class WorkerRunner:
    def __init__(self, name, url):
        try:
            self._name = name
            self._sock = nn.Socket(nn.REP)
            self._sock.connect(url)
        except nn.NanoMsgError:
            traceback.print_exc()
            raise

    def __del__(self):
        if self._sock.is_open():
            self._sock.close()

    def run(self):
        if self._sock.is_open():
            try:
                while True:
                    msg = self._sock.recv()
                    print("%s,%s" % (self._name, msg))
                    self._sock.send(msg)
            except nn.NanoMsgError:
                traceback.print_exc()
                raise

        else:
            raise "socket error"


if __name__ == '__main__':
    p = PyWorker("worker1")
    p.run()
