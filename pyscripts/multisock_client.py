import nanomsg as nn
from time import sleep
import threading


def run(name, time_for_sleep):
    try:
        sock = nn.Socket(nn.REQ)
        sock.connect("tcp://localhost:5556")
        i = 1
        while True:
            msg = "%s,%d" % (name, i)
            sock.send(msg)
            print(sock.recv())
            i += 1
            sleep(time_for_sleep)
    except nn.NanoMsgError:
        raise
    finally:
        sock.close()


def main():
    time_for_sleep = int(input())
    threads = []
    for i in range(100):
        name = "Client %d" % i
        t = threading.Thread(target=run, args=(name, time_for_sleep));
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
