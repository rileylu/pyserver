from abc import ABCMeta, abstractmethod
import nanomsg as nn
import threading
import traceback


class Runner(threading.Thread):
    __metaclass__ = ABCMeta

    def __init__(self, url):
        super().__init__()
        self._url = url

    def __del__(self):
        try:
            self._sock.close()
        except:
            traceback.print_exc()
            raise

    def __call__(self, *args, **kwargs):
        try:
            sock = nn.Socket(nn.REP)
            sock.connect(self._url)
            while True:
                req = sock.recv()
                rep = self._run(req)
                sock.send(rep)
        except nn.NanoMsgError:
            traceback.print_exc()
            raise

    @abstractmethod
    def _run(self, req):
        pass
