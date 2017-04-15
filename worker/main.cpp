#include <nanomsg/nn.h>
#include <nanomsg/reqrep.h>
#include <cassert>
#include <string>
#include <iostream>

int main(int argc, char *argv[])
{
    std::string name;
    std::cin>>name;

    int sock=nn_socket(AF_SP,NN_REP);
    assert(sock>=0);
    int sock_port=nn_connect(sock,"tcp://localhost:5557");
    assert(sock_port>=0);
    while(true)
    {
        void *msg=nullptr;
        int bytes=nn_recv(sock,&msg,NN_MSG,0);
        if(bytes>0)
        {
            std::string s{static_cast<char*>(msg)};
            s.erase(bytes);
            std::cout<<name<<" : "<<s<<std::endl;
            nn_send(sock,msg,bytes,0);
        }
    }
}
