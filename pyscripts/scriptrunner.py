from worker import PyWorker
from runner import Runner


class ScriptRunner(Runner):
    def _run(self, req):
        print(req)
        return req


if __name__ == '__main__':
    runner = ScriptRunner("worker", "tcp://localhost:5557")
    p = PyWorker("worker1", runner)
    p.run()
