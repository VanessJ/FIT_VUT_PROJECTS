/**
 * VUT FIT ISA 2021 Project - Reverse engineering of unknown protocol
 * @file client.cpp
 * @author Vanessa Jóriová (xjorio00)
 * @brief implementation of socket communication with server
 */

#include "arg_parser.hpp"
#include "client.hpp"

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <netdb.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>

#include <arpa/inet.h>



void Client::setArgparser(ArgParser aP){
    argParser = aP;

}

int Client::sendRequest(string * request){
    int total = 0;
    const char * c_string = request->c_str();
    int len = strlen(c_string);
    int bytesleft = len;
    int n = 0;
    while(total < len) {
        n = send(sockfd, c_string+total, bytesleft, 0);
        if (n == -1) {
            cerr << "ERROR sending request\n";
            return -1; }
        total += n;
        bytesleft -= n;
    }

    return 0;
}

int Client::getResponse(string * response){
    bool empty = false;
    bzero(buffer, BUFFER_SIZE);
    while(!(empty)){
        int n = recv(sockfd, buffer, BUFFER_SIZE-1, 0);
        if (n < 0){
            cerr << "ERROR reading from socket"; 
            return -1;
    }
        if (buffer[0] == '\0'){
            empty = true;
        }
        
        response->append(string(buffer));
        bzero(buffer, BUFFER_SIZE);
    }
    return 0;
    close(sockfd);

}



void * Client::get_in_addr(struct sockaddr *sa){
    if (sa->sa_family == AF_INET) {
        return &(((struct sockaddr_in*)sa)->sin_addr);
    }

    return &(((struct sockaddr_in6*)sa)->sin6_addr);
}

int Client::connectToServer(){


    string adress = argParser.getIPAdress();
    const char * char_adress = adress.c_str();
    port_no = argParser.getPort();
    char port_char[100];
    sprintf(port_char,"%d",port_no);

    struct addrinfo hints, *servinfo, *p;
    int rv;
    char s[INET6_ADDRSTRLEN];
    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;

    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;

    if ((rv = getaddrinfo(char_adress, port_char, &hints, &servinfo)) != 0) {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(rv));
        return 1;
    }

    for (p = servinfo; p != NULL; p = p->ai_next) {
        if ((sockfd = socket(p->ai_family, p->ai_socktype,
                p->ai_protocol)) == -1) {
            perror("client: socket");
            continue;
        }

        if (connect(sockfd, p->ai_addr, p->ai_addrlen) == -1) {
            close(sockfd);
            perror("client: connect");
            continue;
        }

        break;
    }

    if (p == NULL) {
        fprintf(stderr, "client: failed to connect\n");
        return -1;
    }

    inet_ntop(p->ai_family, get_in_addr((struct sockaddr *)p->ai_addr),
            s, sizeof s);
    //printf("client: connecting to %s\n", s);



    freeaddrinfo(servinfo); 


    return 0;
}