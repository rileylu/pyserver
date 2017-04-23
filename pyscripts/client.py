import nanomsg as nn
import traceback
from time import sleep

from proto.pyscript_pb2 import *

name = str(input())
sleep_for = int(input())

try:
    sock = nn.Socket(nn.REQ)
    sock.connect("tcp://localhost:5556")
    i = 0
    while True:
        req = Request()
        req.script = "print('haha')"
        sock.send(req.SerializeToString())
        rep = Response()
        rep.ParseFromString(sock.recv())
        print(rep.result)
        i += 1
        sleep(sleep_for)
except nn.NanoMsgError:
    traceback.print_exc()
    raise
finally:
    sock.close()
