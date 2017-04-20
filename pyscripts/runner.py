from abc import ABCMeta, abstractmethod
import nanomsg as nn
import traceback
import threading


def func(url,fun):
    try:
        sock = nn.Socket(nn.REP)
        sock.connect(url)
        while True:
            req = sock.recv()
            rep = fun(req)
            sock.send(rep)
    except nn.NanoMsgError:
        traceback.print_exc()
        raise
    finally:
        if sock.is_open():
            sock.close()


class Runner:
    __metaclass__ = ABCMeta

    def __init__(self, func,args, name=threading.current_thread().name):
        self._name = name
        self._func=func
        self._args=args

    def __call__(self, url):
        self._func(*self._args)

    @abstractmethod
    def _run(self, req):
        pass
