/**
 * VUT FIT ISA 2021 Project - Reverse engineering of unknown protocol
 * @file response_parser.hpp
 * @author Vanessa Jóriová (xjorio00)
 * @brief transforms server response for output
 */


#ifndef RESPONSE_PARSER_HPP
#define RESPONSE_PARSER_HPP

#include "arg_parser.hpp"
#include <iostream>

using namespace std;

class ResponseParser{
    private:
        string * response;
        int current_index;

        /**
         * @param token session token
         */ 
        void writeToken(string * token);

        /**
         * @param str server response
         * @return current position in string or -1 in case of unexpected server response
         */ 
        int checkStatus(string * str);

        /**
         * @return amount of whate spaces skipped
         */ 
        int skipWhiteSpace();
        
        /**
         * @return true if left bracket on current index, false if not
         */ 
        bool checkLBracket();

        /**
         * @return true if right bracket on current index, false if not
         */ 
        bool checkRBracket();

        /**
         * @return true if question marks on current index, false if not
         */ 
        bool checkQMarks();
        bool error = false;

        /**
         * @param old_str response from server with special escaped chars
         * @return correctly escaped string for output 
         */
        string * outputParse(string * old_str);

        /**
         * unction gets substring from beggining until first occurence of question marks (escaped question marks are ignored)
         * @param current_index current index
         * @param str original string
         * @param found_string found substring
         * @return new index or -1 in case of error
         */ 
        int stringUntilQMarks(int current_index, string * str, string * found_string);

        /**
         * function gets substring from beggining until first occurence of whitespace
         * @param str original string
         * @param found_string found substring
         * @return new index or -1 in case of error
         */ 
        int stringUntilWhiteSpace(string * str, string * found_string);


    public:

        ResponseParser(string * str);
        int ParseResponse(ArgParser argParser, string * response);

};



#endif