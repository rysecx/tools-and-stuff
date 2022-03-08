#!/bin/python3
# server script

import sys
import socket
import time


def server_start():
    host = '192.168.0.0'
    port = 50222
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f'server listening on {host}::{port}')
    # recieving filesize
    clientSock, clientAddr = s.accept()
    print(f'recieved connection from {clientAddr}')
    filesize = clientSock.recv(1024)
    filesize = filesize.decode()
    filesize = int(filesize)
    fileData = ''
    time.sleep(0.2)
    if filesize > 1448:
        fragmentCount = filesize / 1448
        fragmentCount += 1
    else:
        fragmentCount = 1
    for i in range(int(fragmentCount)):
        fileBytes = clientSock.recv(1500)
        fileBytes = fileBytes.decode()
        fileData += fileBytes
        print(f'recieving bytes: {len(fileData)}/{filesize}')
        if filesize == len(fileData):
            print(f'recieved bytes successfully')
            ok = '200'
            time.sleep(0.2)
            clientSock.send(ok.encode())
            time.sleep(0.2)
            sys.exit()
        else:
            print('filebytes missing')
            pass

try:
    server_start()

except Exception as error:
    print(f'ERROR: {error}')
    sys.exit()
