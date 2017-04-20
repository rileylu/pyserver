import nanomsg as nn
import traceback
from time import sleep

name = str(input())
sleep_for = int(input())

try:
    sock = nn.Socket(nn.REQ)
    sock.connect("tcp://localhost:5556")
    i = 0
    while True:
        msg = "%s,%d" % (name, i)
        sock.send(msg)
        print(sock.recv())
        i += 1
        sleep(sleep_for)
except nn.NanoMsgError:
    traceback.print_exc()
    raise
finally:
    sock.close()
