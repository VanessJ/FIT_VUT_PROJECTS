/**
 * VUT FIT ISA 2021 Project - Reverse engineering of unknown protocol
 * @file arg_parser.hpp
 * @author Vanessa Jóriová (xjorio00)
 * @brief command line arguments processing
 */



#ifndef ARGS_HPP

#define ARGS_HPP
#include <iostream>
using namespace std;
#define HELP 20

enum action_enum{DEFAULT, REGISTER, LOGIN, LIST, SEND, FETCH, LOGOUT};


/**
 * Class parsing command line arguments
 */
class ArgParser{
    private:
        string * ipAdress; 
        int port;
        bool adressSet = false;
        bool portSet = false;
        int action = DEFAULT;
        string * username;
        string * password;
        string * recipient;
        string * subject;
        string * body;
        string * id;

        /**
         * @param index of port number in arguments arrat
         * @param argv command line arguments
         * @return port number, -1 if port number is not a string, -2 if port number does not belong into 0-65535 range
         */ 
        int parsePort(int index, char *argv[]);
        
        
        /**
         * prints help
         */ 
        void printHelp();

        /**
         * checking if given switch exists
         * @param begin beginning
         * @param end end
         * @param option given switch 
         * @return true if switch found, false if not 
         * Inspired by: https://stackoverflow.com/a/868894
         */ 
        bool cmdOptionExists(char** begin, char** end, const std::string& option);

    public:
        /**
         * constructor 
         */
        ArgParser();

        /**
         * parsing of command line arguments
         * @param argc number of command line arguments
         * @param argv vector of command line arguments
         * @return action or -1 in case of incorrect command line arguments, constant HELP in case of "help" switch, else 0
         */ 
        int parseArgs(int argc, char *argv[]);
        
        /**
         * @return IP adress
         */ 
        string getIPAdress();

         /**
         * @return port number
         */ 
        int getPort();

        /**
         * @return action number
         */ 
        int getAction();

        /**
         * @return username
         */ 
        string getUsername();

        /**
         * @return password
         */ 
        string getPassoword();

        /**
         * @return recipient of messege
         */ 
        string getRecipient();

        /**
         * @return subject of messege
         */ 
        string getSubject();

        /**
         * @return body of messege
         */ 
        string getBody();

        /**
         * @return id of given messege
         */ 
        string getId();

};




#endif
 