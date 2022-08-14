/**
 * VUT FIT ISA 2021 Project - Reverse engineering of unknown protocol
 * @file request_parser.cpp
 * @author Vanessa Jóriová (xjorio00)
 * @brief request creation and formatting based on command line arguments parameters
 */
#include "arg_parser.hpp"
#include "request_parser.hpp"

#include <iostream>
#include <fstream>
using namespace std;


RequestParser::RequestParser(ArgParser ap){
    argParser = ap;

}
string * RequestParser::ParseRequest(){
    int action = argParser.getAction();
    string * full_request = new string();
    string * name;
    string * recipient;
    string * subject;
    string * body;
    string * encoded_password;
    switch(action){
        case REGISTER: 
            name = new string(argParser.getUsername());
            parseString(name);
            encoded_password = new string(base64_encode((argParser.getPassoword())));
            full_request->append("(register \"" + *name + "\" \"" + *encoded_password + "\")");
            break;
        case LOGIN:
            name = new string(argParser.getUsername());
            parseString(name);
            encoded_password = new string(base64_encode((argParser.getPassoword())));
            full_request->append("(login \"" + *name + "\" \"" + *encoded_password + "\")");
            break;
        case LIST:
            if (!checkIfLoggedIn()){
                return full_request;
            }
            readToken();
            full_request->append("(list "  + login_token + ")");
            break;
        case SEND:
            
            if (!checkIfLoggedIn()){
                return full_request;
            }
            readToken();
            recipient = new string(argParser.getRecipient());
            parseString(recipient);
            subject = new string(argParser.getSubject());
            parseString(subject);
            body = new string(argParser.getBody());
            parseString(body);
            full_request->append(  \
            "(send "  + login_token + " \"" + *recipient + "\" \"" + *subject + "\" \"" + *body + "\")" \
            );
            break;
        case FETCH:

            if (!checkIfLoggedIn()){
                return full_request;
            }
            readToken();
            full_request->append("(fetch "  + login_token + " " + argParser.getId() + ")");
            break;
        case LOGOUT:
            if (!checkIfLoggedIn()){
                return full_request;
            }
            readToken();
            full_request->append("(logout "  + login_token + ")");
            break;
        default:
            break;
    }

    return full_request; 
}
bool RequestParser::checkIfLoggedIn(){
    ifstream f("login-token");
    return f.good();
    
}
void RequestParser::readToken(){
    ifstream infile("login-token");
    if (infile.good()){
        string sLine;
        getline(infile, sLine);
        login_token = sLine;
    }
    else {
        cerr << "ERROR: internal error";
        exit(-1);
    }
  infile.close();

}


void RequestParser::parseString(string * s){
    for (size_t i = 0; i < s->length(); i++){
        char c = (*s)[i];
        switch(c){
            case '\"':
                s->replace(i,1, "\\\"");
                ++i;
                break;
            case '\\':
                s->replace(i,1, "\\\\");
                ++i;
                break;
            case '\n':
                s->replace(i,1, "\\n");
                ++i;
                break;
        }

    }

}


string RequestParser::base64_encode(const string &in) {

    string out;

    int val = 0, valb = -6;
    for (unsigned char c : in) {
        val = (val << 8) + c;
        valb += 8;
        while (valb >= 0) {
            out.push_back("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"[(val>>valb)&0x3F]);
            valb -= 6;
        }
    }
    if (valb>-6) out.push_back("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"[((val<<8)>>(valb+8))&0x3F]);
    while (out.size()%4) out.push_back('=');
    return out;
}
