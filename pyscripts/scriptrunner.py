from worker import PyWorker
from runner import Runner


class ScriptRunner(Runner):
    def _run(self, req):
        print(req)
        return req


if __name__ == '__main__':
    r = ScriptRunner("tcp://localhost:5557")
    p = PyWorker(worker_id="worker1", runner=r)
    p.run()
