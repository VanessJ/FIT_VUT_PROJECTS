/**
 * VUT FIT ISA 2021 Project - Reverse engineering of unknown protocol
 * @file response_parser.cpp
 * @author Vanessa Jóriová (xjorio00)
 * @brief transforms server response for output
 */

#include "arg_parser.hpp"
#include "response_parser.hpp"

#include <iostream>
#include <string.h>
#include <fstream>

#define QMARKSKIP 3


int ResponseParser::ParseResponse(ArgParser argParser, string * response){
    int action = argParser.getAction();
    string status; 
    string * found_string = new string("");
    int first_index;
    int skipped;
    int result;
    bool stop;
    char c;
    switch(action){
        case REGISTER:
            status = response->substr(1,3);
            if (status == "ok "){
                cout << "SUCCESS: ";
            }
            else if (status == "err"){
                status = response->substr(1,3);
                cout << "ERROR: ";
            }
            else {
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }

            if (status == "ok "){
                first_index = 5;
            }
            else {
                first_index = 6;
            }

            current_index = stringUntilQMarks(first_index,response,found_string);
            if (current_index < 0){
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }
            else{
                found_string = outputParse(found_string);
                cout << *found_string << "\n";
            }
        
            break;


        case LOGIN:
            status = response->substr(1,3);
            if (status == "ok "){
                cout << "SUCCESS: ";
            }
            else if (status == "err"){
                status = response->substr(1,3);
                cout << "ERROR: ";
            }
            else {
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }
            if (status == "ok "){
                first_index = 5;
            }
            else {
                first_index = 6;
            }


            current_index = stringUntilQMarks(first_index, response,found_string);
            if (current_index< 0){
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }
            else{
                found_string = outputParse(found_string);
                cout << *found_string << "\n";
                if (status == "err"){
                    return 0;
                }
            }

            *found_string = "";
            result = stringUntilQMarks(current_index + QMARKSKIP, response,found_string);
            if (result< 0){
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }
            else{
                writeToken(found_string);
            }

            break;

        case LIST:
            current_index = checkStatus(response);
            if (current_index < 0){
                cerr <<"ERROR: Unexpected server response\n";
                return -1;
            }

            if (error){
                current_index = skipWhiteSpace();
                if (!checkQMarks()){
                    return -1;
                }

                current_index = stringUntilQMarks(current_index,response,found_string);
                if (current_index < 0){
                    cerr << "ERROR: Unexpected server response\n";
                    return -1;
                }
                found_string = outputParse(found_string);
                cout << *found_string << "\n";
                return 0;

            }

            current_index = skipWhiteSpace();
            if (!checkLBracket()){
                return -1;
            }
            stop = false;
            
            while(true){
                current_index = skipWhiteSpace();
            
            c = (*response)[current_index];
            if (c == ')'){
                cout <<"\n";
                break;
            }
            else if (c != '('){
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }

            current_index++;
            * found_string = "";
            current_index = stringUntilWhiteSpace(response,found_string);
            if (current_index < 0){
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }
            found_string = outputParse(found_string);
            cout << "\n" << *found_string << ":\n";
            current_index = skipWhiteSpace();

            if(!checkQMarks()){
                return -1;
            }

            * found_string = "";
            current_index = stringUntilQMarks(current_index, response,found_string);
            if (current_index < 0){
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }
            found_string = outputParse(found_string);
            cout << "  From: " << *found_string << "\n";
            
            if(!checkQMarks()){
                return -1;
            }
            current_index = skipWhiteSpace();

            if(!checkQMarks()){
                return -1;
            }
            * found_string = "";
            current_index = stringUntilQMarks(current_index, response,found_string);
            if (current_index < 0){
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }
            found_string = outputParse(found_string);
            cout << "  Subject: " << *found_string << "\n";
            
            
            if(!checkQMarks()){
                return -1;
            }

            if(!checkRBracket()){
                return -1;
            }

            current_index = skipWhiteSpace();    
            
            }

            break;
        case SEND:
            current_index = checkStatus(response);
            if (current_index < 0){
                cerr <<"ERROR: Unexpected server response\n";
                return -1;
            }

            if (error){
                current_index = skipWhiteSpace();
                if (!checkQMarks()){
                    return -1;
                }

                current_index = stringUntilQMarks(current_index,response,found_string);
                if (current_index < 0){
                    cerr << "ERROR: Unexpected server response\n";
                    return -1;
                }
                found_string = outputParse(found_string);
                cout << *found_string << "\n";
                return 0;

            }

            current_index = skipWhiteSpace();
            if (!checkQMarks()){
                return -1;
            }
            current_index = stringUntilQMarks(current_index,response,found_string);
            if (current_index < 0){
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }
            else{
                found_string = outputParse(found_string);
                cout << *found_string << "\n";
            }
            if(!checkQMarks()){
                return -1;
            }

            if (!checkRBracket()){
                return -1;
            }
            break;
        case FETCH:

            current_index = checkStatus(response);
            if (current_index < 0){
                cerr <<"ERROR: Unexpected server response\n";
                return -1;
            }
            current_index = skipWhiteSpace();

            if (error){
                if (!checkQMarks()){
                    return -1;
                }

                current_index = stringUntilQMarks(current_index,response,found_string);
                if (current_index < 0){
                    cerr << "ERROR: Unexpected server response\n";
                    return -1;
                }
                found_string = outputParse(found_string);
                cout << *found_string << "\n";
                return 0;

            }
        
            if (!checkLBracket()){
                return -1;
            }

            if (!checkQMarks()){
                return -1;
            }

            current_index = stringUntilQMarks(current_index,response,found_string);
            if (current_index < 0){
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }

            cout << "\n\n";
            found_string = outputParse(found_string);
            cout << "From: " << *found_string << "\n";

            if (!checkQMarks()){
                return -1;
            }
            current_index = skipWhiteSpace();
            if (!checkQMarks()){
                return -1;
            }

            * found_string = "";
            current_index = stringUntilQMarks(current_index,response,found_string);
            if (current_index < 0){
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }
            found_string = outputParse(found_string);
            cout << "Subject: " << *found_string << "\n";


            if (!checkQMarks()){
                return -1;
            }
            current_index = skipWhiteSpace();
            if (!checkQMarks()){
                return -1;
            }

            * found_string = "";
            current_index = stringUntilQMarks(current_index,response,found_string);
            if (current_index < 0){
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }
            found_string = outputParse(found_string);
            cout << "\n";
            cout << *found_string;


            
            break;
        case LOGOUT:
            status = response->substr(1,3);
            if (status == "ok "){
                cout << "SUCCESS: ";
            }
            else if (status == "err"){
                status = response->substr(1,3);
                cout << "ERROR: ";
            }
            else {
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }

            if (status == "ok "){
                first_index = 5;
            }
            else {
                first_index = 6;
            }

            current_index = stringUntilQMarks(first_index,response,found_string);
            if (current_index < 0){
                cerr << "ERROR: Unexpected server response\n";
                return -1;
            }
            else{
                found_string = outputParse(found_string);
                cout << *found_string << "\n";
            }
        

            if (remove("login-token") != 0){
                cerr <<"Error deleting file";
                return -1;
            }
            break;
        default:
            break;
    }

    return 0;
}

void ResponseParser::writeToken(string * token){
    ofstream file ("login-token");
    if (file.is_open()){
        file << "\"" << *token << "\"" << "\n";
        file.close();
    }


}


int ResponseParser::checkStatus(string * str){
    if (!checkLBracket()){
        return -1;
    }
    string status = str->substr(1,2);
    if (status == "ok"){
        cout << "SUCCESS: ";
        error = false;
    }
    else if (status == "er"){
        status = str->substr(1,3);
        if (status == "err"){
          cout << "ERROR: "; 
          error = true; 
        }
    }
    else {
        cerr << "ERROR: Unexpected server response\n";
        return -1;
    }

    if (status == "ok"){
        return 3;
    }

    else {
        return 4;
    }

}


string * ResponseParser::outputParse(string * old_string){
    string * parsed_string = new string("");
    char c;
    for (int i = 0; i < old_string->length(); i++ ){
        c = (*old_string)[i];
        if (c == '\\'){
            c = (*old_string)[++i];
            if (c == 'n'){
                parsed_string->append("\n");
            }
            if (c == '\"'){
                parsed_string->append("\"");
            }

            if (c == '\\'){
                parsed_string->append("\\");
            }
        }
        else {
            parsed_string->push_back(c);
        }    
    }

    return parsed_string;
}
bool ResponseParser::checkLBracket(){
    char c;
    c = (*response)[current_index];
    if (c != '(' ){
        return false;
    }
    current_index++;
    return true;

}


bool ResponseParser::checkQMarks(){
    char c;
    c = (*response)[current_index];
    if (c != '\"' ){
        return false;
    }
    current_index++;
    return true;
}

bool ResponseParser::checkRBracket(){
    char c;
    c = (*response)[current_index];
    if (c != ')' ){
        return false;
    }
    current_index++;
    return true;

}


int ResponseParser::skipWhiteSpace(){
    char c;
    bool white_space = true;
    int i = current_index;
    while(white_space){
        c = (*response)[i];
        if (c != ' '){
            break;
        }
        ++i;
        if (i > (response->length()-1)){
            return -1;
        }

    }
    return i;
}


ResponseParser::ResponseParser(string * str){
    response = str;
    current_index = 0;
}


int ResponseParser::stringUntilWhiteSpace(string * str, string * found_string){
    char c;
    int i = current_index;
    while(true){
       c = (*str)[i]; 
       if (c == ' '){
           break;
       }
       found_string->push_back(c);
        i++;
        if (i > str->length()){
            cerr << "Invalid response format\n";
            return -1;
        }
    }
    return i;
}



int ResponseParser::stringUntilQMarks(int i, string * str, string * found_string){
    char c;
    bool ignoreQMark = false;
    while(true){
        c = (*str)[i];
        if ((c == '\\') && ignoreQMark){
            ignoreQMark = false;
        }
        else if (c == '\\'){
            ignoreQMark = true;
        }

        else if ((c == '\"') && !(ignoreQMark)){
            break;
        }

        else if (ignoreQMark){
            ignoreQMark = false;
        }

        found_string->push_back(c);
        i++;
        if (i > str->length()){
            cerr << "Invalid response format\n";
            return -1;
        }
    }
    return i;
}