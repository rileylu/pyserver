from worker import Runner
from worker import PyWorker


class ScriptRunner(Runner):
    def run(self):
        while True:
            msg = super(ScriptRunner, self)._sock.recv()
            print("%s,%s" % (super(ScriptRunner, self)._name, msg))
            super(ScriptRunner, self)._sock.send(msg)


if __name__ == '__main__':
    runner = ScriptRunner("worker", "tcp://localhost:5557")
    p = PyWorker("worker1", runner)
    p.run()
