from worker import PyWorker
from runner import Runner
from proto.pyscript_pb2 import *


class ScriptRunner(Runner):
    def _run(self, req):
        r=Request()
        r.ParseFromString(req)
        res=Response()
        res.result=exec r.script
        return res.SerializeToString()

if __name__ == '__main__':
    r = ScriptRunner("tcp://localhost:5557")
    p = PyWorker(worker_id="worker1", runner=r)
    p.run()
