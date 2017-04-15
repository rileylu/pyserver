import nanomsg as nn
from time import sleep

name = str(input())
time_to_sleep = int(input())

try:
    sock = nn.Socket(nn.REQ)
    sock.connect("tcp://localhost:5556")
    i = 1
    while True:
        msg = "%s,%d" % (name, i)
        sock.send(msg)
        print(sock.recv())
        i += 1
        sleep(time_to_sleep)
except nn.NanoMsgError:
    raise
finally:
    sock.close()
