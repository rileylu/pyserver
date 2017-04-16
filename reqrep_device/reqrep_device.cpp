#include "reqrep_device.h"
#include <nanomsg/nn.h>
#include <nanomsg/reqrep.h>
#include <cassert>
#include <iostream>

void reqrep_device()
{
	int rep = nn_socket(AF_SP_RAW,NN_REP);
	assert(rep>=0);
	int rep_port = nn_bind(rep, "tcp://*:5556");
	assert(rep_port>=0);

	int req = nn_socket(AF_SP_RAW,NN_REQ);
	assert(req>=0);
	int req_port = nn_bind(req, "tcp://*:5557");
	assert(req_port>=0);

	int rc = nn_device(rep, req);

	if (rc < 0 && nn_errno() == ETERM)
	{
		std::cerr << "terminated." << std::endl;
	}
	nn_close(rep);
	nn_close(req);
}
