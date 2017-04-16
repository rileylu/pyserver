#include "../reqrep_device/reqrep_device.h"
#include "../worker/worker.h"
#include <thread>
#include <vector>
#include <algorithm>
#include <string>

int main()
{
	std::thread rrdevice(reqrep_device);
	std::vector<std::thread> workers;
	for (int i = 0; i < 4; ++i)
	{
		workers.emplace_back(worker,std::string("worker").append(std::to_string(i)));
	}
	rrdevice.join();
	std::for_each(workers.begin(), workers.end(), [](std::thread& t) { t.join(); });
	return 0;
}