import nanomsg as nn

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
