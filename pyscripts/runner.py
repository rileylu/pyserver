from abc import ABCMeta, abstractmethod
import nanomsg as nn
import traceback


class Runner:
    __metaclass__ = ABCMeta

    def __init__(self, name, url):
        self._name = name
        self._url = url

    def run(self):
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
        finally:
            if sock.is_open():
                sock.close()

    @abstractmethod
    def _run(self, req):
        pass
