from worker import PyWorker
from runner import Runner


class ScriptRunner(Runner):
    def _run(self, req):
        print(req)
        return req


if __name__ == '__main__':
    r = ScriptRunner()
    p = PyWorker(worker_id="worker1", runner=r, url="tcp://localhost:5557")
    p.run()
