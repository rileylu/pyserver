import traceback
from multiprocessing import cpu_count
import threading


class PyWorker:
    def __init__(self, worker_id, runner, url):
        self._id = worker_id
        self._threads = []
        try:
            for i in range(cpu_count()):
                self._threads.append(threading.Thread(target=runner(url)))
        except Exception:
            traceback.print_exc()
            raise

    def run(self):
        try:
            for t in self._threads:
                t.start()
            for t in self._threads:
                t.join()
        except Exception:
            traceback.print_exc()
            raise
