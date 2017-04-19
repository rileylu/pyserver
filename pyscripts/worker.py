import nanomsg as nn
import traceback
import pyexecutor_pb2 as proto



class PyExecutor:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._sock = None

    def _connect(self):
        try:
            self._sock = nn.Socket(nn.REP)
            self._sock.connect("tcp://%s:%s" % (self._host, self._port))
        except nn.NanoMsgError:
            traceback.print_exc()
            raise

    def _close(self):
        try:
            if self._sock:
                self._sock.close()
        except nn.NanoMsgError:
            traceback.print_exc()
            raise

    def run(self):
        self._connect()
        while True:
            msg = self._sock.recv()
            s=proto.Request()
            request=s.ParseFromStream(msg)
            #do something
            response=proto.Response()
            res=response.SerializeToString()
            print("%s" % res)
            self._sock.send(res)

    def __del__(self):
        self._close()


if __name__ == "__main__":
    name = str(input())

    try:
        sock = nn.Socket(nn.REP)
        sock.connect("tcp://localhost:5557")
        while True:
            msg = sock.recv()
            print("%s,%s" % (name, msg))
            sock.send(msg)

    except nn.NanoMsgError:
        raise
    finally:
        sock.close()
