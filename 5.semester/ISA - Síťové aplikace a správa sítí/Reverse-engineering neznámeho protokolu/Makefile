
CC=g++

CFLAGS=-std=c++11 -Wall -Wextra 


PROJ=main

CODE = arg_parser.cpp arg_parser.hpp client.cpp client.hpp main.cpp request_parser.cpp request_parser.hpp response_parser.cpp response_parser.hpp


client: $(PROJ).o arg_parser.o client.o request_parser.o response_parser.o
	$(CC) $(CFLAGS) $(PROJ).o arg_parser.o request_parser.o client.o response_parser.o -o client

$(PROJ).o: $(PROJ).cpp 
	$(CC) $(CFLAGS) -c $(PROJ).cpp -o $(PROJ).o

client.o: client.cpp client.hpp
	$(CC) $(CFLAGS) -c client.cpp -o client.o

request_parser.o: request_parser.cpp request_parser.hpp
	$(CC) $(CFLAGS) -c request_parser.cpp -o request_parser.o

response_parser.o: response_parser.cpp response_parser.hpp
	$(CC) $(CFLAGS) -c response_parser.cpp -o response_parser.o

arg_parser.o: arg_parser.cpp arg_parser.hpp
	$(CC) $(CFLAGS) -c arg_parser.cpp -o arg_parser.o


clean:
	rm -f *.o

tar:
	tar -cf xjorio00.tar Makefile README manual.pdf isa.lua isa.pcap  $(CODE) 