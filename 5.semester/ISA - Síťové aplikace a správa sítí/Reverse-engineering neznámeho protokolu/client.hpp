/**
 * VUT FIT ISA 2021 Project - Reverse engineering of unknown protocol
 * @file client.hpp
 * @author Vanessa Jóriová (xjorio00)
 * @brief implementation of socket communication with server
 * socket communication inspired by: https://beej.us/guide/bgnet/html/#client-server-background
 */

#ifndef CLIENT_HPP

#define CLIENT_HPP

#include "arg_parser.hpp"

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

#define BUFFER_SIZE 1000

using namespace std;

class Client{
    private:
        ArgParser argParser;
        int sockfd; 
        int port_no;
        int action;
        struct sockaddr_in serv_addr;
        struct hostent *server;
        char buffer[BUFFER_SIZE];

        /**
         * @param sa struct with adress
         */ 
        void *get_in_addr(struct sockaddr *sa);

        

    public:

        /**
         * @return 0 if succes, else -1
         */
        int connectToServer();

        /**
         * @param request formatted request
         * @return 0 if successful, else -1
         */ 
        int sendRequest(string * request);

        /**
         * @param response obtained response
         * @return 0 if successful, else -1
         */ 
        int getResponse(string * response);

        /**
         * @param aP instance of argParser with all the necessary information
         *           from command line arguments
         */ 
        void setArgparser(ArgParser aP);


};

#endif