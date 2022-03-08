#!/bin/python3
# client script

import sys
import time
import socket

def client_start():
    if len(sys.argv) == 3 and sys.argv[1] == '--f':
        file = sys.argv[2]
        with open (file, 'rb') as openFile:
            bytes = openFile.read()
        openFile.close()
        print('connecting to server...', end='\r')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '192.168.0.0'
        port = 50222
        s.connect((host, port))
        print('connected to server done')
        print('sending file not encrypted...')
        filesize = len(bytes)
        filesize = str(filesize)
        s.send(filesize.encode())
        time.sleep(0.2)
        s.send(bytes)
        answ = s.recv(1024)
        answ = answ.decode()
        if answ == '200':
            print('#' * 100)
            print('# Success. Well done! Everyone in your network could read your confidental package! F*ck security! #' )
            print('#' * 100)

            s.close()
            sys.exit()
        else:
            print('Something went wrong. quitting')
            s.close()
            sys.exit()
    else:
        print('usage: ./noencrcli.py --f [FILE]')
    
try: 
    client_start()

except Exception as error:
    print(f'ERROR: {error}')
    sys.exit()
