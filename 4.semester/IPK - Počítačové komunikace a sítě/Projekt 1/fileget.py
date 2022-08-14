#!/usr/bin/env python3.8

"""
Brief:  IPK 2020/21 assigment - network client that downloads files and saves them in local directory 
Author: Vanessa Jóriová, xjorio00
Date: 30.3.2021

Details:    Network client that downloads files from server and saves them in current directory.
            Usable with: fileget -n NAMESERVER -f SURL arguments
            Example: ./fileget.py -n 127.0.0.1:3333 -f fsp://muj.server.number.one/*

            GET:
                Downloads one specified file. Requires complete directory path.
            GET ALL:
                Dowloads all files from server. Only basic functionality is supported, all files are saved in local directory.

"""


import argparse, sys, socket, re, os, sys

def arg_parse():
    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", action="store", type=str, dest="nameserver", required=True)
        parser.add_argument("-f", action="store", type=str, dest="surl", required=True)
        arguments = parser.parse_args()
        return arguments

def get_host_port(ip):
    try: 
        splitted = ip.split(":");
        if (len(splitted) != 2):
            sys.exit("Wrong format of nameserver adress\n")
        host = splitted[0]
        port = int(splitted[1])
    except ValueError:
        sys.exit("Wrong format of nameserver adress\n")
    
    return host, port



def surl_parse(surl):
    try:
        first_split = surl.split("//")
        if (len(first_split) != 2):
            sys.exit("Wrong format of surl adress\n")
        protocol = first_split[0]
        if protocol.lower() != "fsp:":
            sys.exit("Unsupported protocol in surl adress\n")
        second_split = first_split[1].split("/", 1)
        if (len(second_split) != 2 ):
            sys.exit("Wrong format of surl adress\n")
        nameserver = second_split[0]
        filepath = second_split[1]
    except ValueError:
        sys.exit("Wrong format of surl adress\n")

    return nameserver, filepath


def get_tcp_adress(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
        try:
            udp.settimeout(30.0);
            udp.connect((host, port));
            udp.sendall(request.encode());
            data = udp.recv(4028)
        except socket.error as e:
            sys.exit("UDP connection failed: " + str(e))
        except socket.timeout:
            sys.exit("UDP connection failed: timeout reached")
        except OverflowError:
            sys.exit("Wrong port: port must be 0-65535")
        finally: 
            udp.close()
    data_decode = data.decode()
    split = data_decode.split(" ", 1)
    if (len(split) < 2):
        sys.exit("Unexpected nameserver response")
    status = split[0]
    msg = split[1]
    if status == "OK":
        host, port = get_host_port(msg)
        return host, port
    elif status.lower() == "err" and msg.lower() == "not found":
        sys.exit("Fileserver not found")
    else :
        sys.exit("Unexpected nameserver response")
    
def process_header(buffer, fileserver, adress):
    if re.search(r"FSP/1\.0 Not Found\r\nLength:\s*\d+", buffer):
        sys.exit(f"{adress} not found on {fileserver}")
    elif re.search(r"FSP/1\.0 Bad Request\r\nLength:\s*\d+", buffer):
        sys.exit(f"Connection to {fileserver} unsuccesful: bad TCP request format")
    elif re.search(r"FSP/1\.0 Server Error\r\nLength:\s*\d+", buffer):
        sys.exit(f"Connection to {fileserver} unsuccesful: server-side error")
    elif not re.search(r"FSP/1\.0 Success\r\nLength:\s*\d+", buffer):
        sys.exit("Unsupported TCP response")
    else:
        split = buffer.split("\r\n")
        length = split[1]
        split2 = length.split(":")
        size = split2[1]
        return size

def write_file(buffer, filename, expected_size):
    try:
        f = open(filename, "wb")
        print("Downloading: " + filename)
        f.write(buffer)
        f.close()
    except IOError as e:
        sys.exit("Unexpected IOError: " + str(e))
    if (filename != "index"):
        #actual_size = os.path.getsize(filename)
        statinfo = os.stat(filename)
        actual_size = statinfo.st_size
        if (int(actual_size) != int(expected_size)):
            print(f"Warning: Size of {filename} differs from expected value. Expected: {expected_size}, actual: {actual_size}. File may be corrupted\n")
        




def download_file(host, port, fileserver, filename, adress):
    request = f"GET {adress} FSP/1.0\r\nHostname: {fileserver}\r\nAgent:xjorio00\r\n\r\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
        try:
            tcp.settimeout(30.0);
            tcp.connect((host, port));
            tcp.sendall(request.encode());
            buffer = bytearray()
            while True:
                data = tcp.recv(4096);
                if not data: break
                buffer.extend(data)

        except socket.error as e:
            sys.exit("TCP connection failed: " + str(e))
        except socket.timeout:
            sys.exit("TCP connection failed: timeout reached")
        except OverflowError:
            sys.exit("Wrong port: port must be 0-65535")
        finally:
            tcp.close()
        split = buffer.split(b"\r\n\r\n", 1)
        header = split[0].decode()
        content = split[1]
        size = process_header(header, fileserver, adress)
        write_file(content, filename, size)

    
    
def surl_split(surl):
    first_split = surl.split("//")
    if (len(first_split) != 2 ):
        sys.exit("Wrong format of surl adress\n")
    second_split = first_split[1].split("/", 1)
    if (len(second_split) != 2 ):
        sys.exit("Wrong format of surl adress\n")
    return_list = [second_split[0], second_split[1]]
    return return_list

def get_filename(filepath):
    splitted = filepath.split("/")
    return splitted[-1]

def main():
    args = arg_parse()
    host, port = get_host_port(args.nameserver)
    nameserver, filepath = surl_parse(args.surl)
    udp_msg = "WHEREIS {}".format(nameserver)
    new_host, new_port = get_tcp_adress(host, port, udp_msg)
    
    if filepath == "*":
        download_file(new_host, new_port, nameserver, "index_tmp", "index")
        try:
            f = open("index_tmp", "r")
        except IOError as e:
            sys.exit("Unexpected IOError: " + str(e))

        lines = f.readlines()
        for line in lines:
            filename = get_filename(line)
            download_file(new_host, new_port, nameserver, filename.rstrip(), line.rstrip())
        try:
            f.close()
            os.remove("index_tmp")
            print("Removing index_tmp")
        except IOError as e:
            sys.exit("Unexpected IOError: " + str(e))

    else:
        filename = get_filename(filepath)
        download_file(new_host, new_port, nameserver, filename, filepath)
    



if __name__ == "__main__":
    main()
