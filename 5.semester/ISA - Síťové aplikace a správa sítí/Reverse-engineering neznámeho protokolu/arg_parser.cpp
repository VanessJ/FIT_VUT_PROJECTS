/**
 * VUT FIT ISA 2021 Project - Reverse engineering of unknown protocol
 * @file arg_parser.cpp
 * @author Vanessa Jóriová (xjorio00)
 * @brief command line arguments processing
 */



#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <string.h>

#include "arg_parser.hpp"

using namespace std;

ArgParser::ArgParser(){
    ipAdress = new string("127.0.0.1");
    port = 32323;

}

string ArgParser::getIPAdress(){
    return * ipAdress;
}

int ArgParser::getPort(){

    return port;
}

int ArgParser::getAction(){
    return action;
}

string ArgParser::getUsername(){
    return * username;
}

string ArgParser::getPassoword(){
    return * password;
}

string ArgParser::getRecipient(){
    return * recipient;
}

string ArgParser::getSubject(){
    return * subject;
}

string ArgParser::getBody(){
    return * body;
}

string ArgParser::getId(){
    return * id;
}




int ArgParser::parseArgs(int argc, char *argv[]){
    if (cmdOptionExists(argv, argv+argc, "-h") or cmdOptionExists(argv, argv+argc, "--help")){
        printHelp();
        return HELP;
    }

    if (argc == 1){
        cerr << "client: expects <command> [<args>] ... on the command line, given 0 arguments\n";
        return -1;   
    }

    for(int i = 1; i < argc; i++){     
        string arg = argv[i];
        if ((arg == "-p") || (arg == "--port")){
            if (portSet){
                cerr << "client: only one instance of one option from (-p --port) is allowed\n";
                return -1;
            }

            if ((i+1) >= argc){
                cerr << "the -p option needs 1 argument, but 0 provided\n";
                return -1;
            }
            int result = parsePort(++i, argv);
            if (result == -1){
                cerr << "Port number is not a string\n";
                return -1;
            }
            if (result == -2){
                cerr << "Port number not in 0-65535 range\n";
                return -1;
            }
            portSet = true;
            port = result;
            continue;
        }

        if ((arg == "-a") || (arg == "--adress")){
            if (adressSet){
                cerr << "client: only one instance of one option from (-a --adress) is allowed\n";
                return -1;
            }

            adressSet = true;
            ipAdress = new string(argv[++i]); 
            continue;        

        }
        
        if (arg == "register"){
            if (argc != (i+3)){
                cerr << "register <username> <password>\n";
                return -1;
            }
            action = REGISTER;
            username = new string(argv[i+1]);
            password = new string(argv[i+2]);
            return action;
        }

        else if (arg == "login"){
            if (argc != (i+3)){
                cerr << "login <username> <password>\n";
                return -1;
            }
            action = LOGIN;
            username = new string(argv[i+1]);
            password = new string(argv[i+2]);
            return action;
        } 

        else if (arg == "list"){
            if (argc != (i+1)){
                cerr << "list\n";
                return -1;
            }
            action = LIST;
            return action;
        } 

        else if (arg == "send"){
            if (argc != (i+4)){
                cerr << "send <recipient> <subject> <body>\n";
                return -1;
            }
            action = SEND;
            recipient = new string(argv[i+1]);
            subject = new string(argv[i+2]);
            body = new string(argv[i+3]);
            return action;
        }

        else if (arg == "fetch"){
            if (argc != (i+2)){
                cerr << "fetcg <id>\n";
                return -1;
            }
            action = FETCH;
            id = new string(argv[i+1]);
            return action;
        }

        else if (arg == "logout"){
            if (argc != (i+1)){
                cerr << "logout\n";
                return -1;
            }
            action = LOGOUT;
            return action;
        }  

        else {
            if (arg[0] == '-'){
                cout << "Unknown switch\n";
                return -1;

            }
            else {
                cout << "Unknown command\n";
            }
            return -1;

            

        }
        

    }

    return action;
}

int ArgParser::parsePort(int index, char *argv[]){
    char * pEnd;
    int portNumber = strtol(argv[index], &pEnd, 10);
    if (*pEnd != '\0'){
       cout << portNumber;
        return -1;
    }
    if ((portNumber < 0) || (portNumber > 65535)){
        return -2;
    }

    return portNumber;
}


bool ArgParser::cmdOptionExists(char** begin, char** end, const std::string& option)
{
    return std::find(begin, end, option) != end;
}

void ArgParser::printHelp()
{
    cout << "usage: client [ <option> ... ] <command> [<args>] ... \n\n";
    cout << "<option> is one of\n\n";
    cout << "  -a <addr>, --address <addr>\n";
    cout << "     Server hostname or address to connect to\n";
    cout << "  -p <port>, --port <port>\n";
    cout << "     Server port to connect to\n";
    cout << "  --help, -h\n";
    cout << "     Show this help\n";
    cout << "  --\n";
    cout << "     Do not treat any remaining argument as a switch (at this level)\n\n";
    cout << " Multiple single-letter switches can be combined after\n";
    cout << " one `-`. For example, `-h-` is the same as `-h --`.\n";
    cout << " Supported commands:\n";
    cout << "   register <username> <password>\n";
    cout << "   login <username> <password>\n";
    cout << "   list\n";
    cout << "   send <recipient> <subject> <body>\n";
    cout << "   fetch <id>\n";
    cout << "   logout\n";

}

