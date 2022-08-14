
#include "arg_parser.hpp"
#include "client.hpp"
#include "request_parser.hpp"
#include "response_parser.hpp"

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

using namespace std;
#define DEBUG false

int main(int argc, char *argv[])
{


    string * response = new string();
    ArgParser argParser;
    int return_value = argParser.parseArgs(argc, argv);
    if (return_value < 0){
        return -1;
    }
    if (return_value == HELP){
        return 0;
    }


    RequestParser requestParser(argParser);
    string * request = requestParser.ParseRequest();
    if (request->length() == 0){
        cout << "Not logged in\n";
        return 0;
    }
    Client client;
    client.setArgparser(argParser);
    return_value = client.connectToServer();
    if (return_value == -1){
        return -1;
    }
    
    return_value = client.sendRequest(request);
    if (return_value <0){
        cerr << "ERROR sending request\n";
        return -1;
    }
    if (DEBUG){
        cout << *request << "\n\n";
    }

    return_value = client.getResponse(response);
        if (return_value <0){
        cerr << "ERROR recieving response\n";
        return -1;
    }
    ResponseParser responseParser(response);
    responseParser.ParseResponse(argParser, response);

    return 0;

    
    

    


 
}