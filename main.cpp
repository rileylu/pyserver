#include "reqrep_device.h"
#include "worker.h"
#include <thread>
#include <vector>
#include <string>
#include <algorithm>

int main(int argc, char *argv[])
{
    std::thread reqrep(reqrep_device);
    std::vector<std::thread> workers;
    for(int i=0;i<4;++i)
        workers.emplace_back(worker,std::string("worker").append(std::to_string(i)));
    if(reqrep.joinable())
        reqrep.join();
    std::for_each(workers.begin(),workers.end(),[](std::thread& t){
        if(t.joinable())
            t.join();
    });
}
