import nanomsg as nn
import traceback
from multiprocessing import cpu_count
import threading


class PyWorker:
    def __init__(self, worker_id, runner):
        self._id = worker_id
        self._threads = []
        try:
            for i in range(cpu_count()):
                self._threads.append(threading.Thread(target=runner.run))
        except Exception:
            traceback.print_exc()
            raise

    def run(self):
        for t in self._threads:
            t.start()
        for t in self._threads:
            t.join()


class Runner:
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
        pass


if __name__ == '__main__':
    p = PyWorker("worker1")
    p.run()
