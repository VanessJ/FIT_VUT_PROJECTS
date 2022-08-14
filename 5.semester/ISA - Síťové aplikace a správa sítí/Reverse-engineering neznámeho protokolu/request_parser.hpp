/**
 * VUT FIT ISA 2021 Project - Reverse engineering of unknown protocol
 * @file request_parser.hpp
 * @author Vanessa Jóriová (xjorio00)
 * @brief request creation and formatting based on command line arguments parameters
 */

#ifndef REQUEST_PARSER_HPP
#define REQUEST_PARSER_HPP

#include "arg_parser.hpp"

#define NOT_LOGGED_IN -2; 


class RequestParser{
    
    private:
        ArgParser argParser;
        string login_token;
        
        /**
         * reads session token 
         */ 
        void readToken();

        /**
         * @return true if user logged in or false if not
         */ 
        bool checkIfLoggedIn();

        /**
         * inspired by: https://stackoverflow.com/a/34571089
         * @param in input string 
         * @return encoded string
         */ 
        string base64_encode(const string &in);
        

    public:
        /**
         * @return parsed request or empty string if user is not logged in
         */ 
        string * ParseRequest();

        /**
         * @param argParser instance of argParser with parsed command line arguments
         */ 
        RequestParser(ArgParser argParser);

        /**
         * checks string for chars that need special escaping for further
         * processing and escapes them
         * @param s unparsed string 
         */
        void parseString(string * s);


};

#endif

