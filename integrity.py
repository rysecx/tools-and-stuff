#!/usr/bin/env python3
import hashlib
import sys
import time
import os


def main():

    print("\r\nintegrity_script is running...\r\n")

    class bcolors:
        GREEN = '\033[92m'
        RED = '\033[91m'
        WHITE = '\033[97m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'

    def encrypt_string(hash_string):
        sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
        return sha_signature

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

    def hashing():

        digit1 = 0
        digit2 = 64
        single_hash = [str(0)]*50

        # linux
        txt_path_ = "/home/usr/Downlaods/hashes.txt"
        txt_path = "/home/usr/Downlaods/"
        txt_file = "hashes.txt"
        dirs = [
            "/bin",
            "/boot",
            "/dev",
            "/etc",
            "/home",
            "/lib",
            "/lib64",
            "/mnt",
            "/opt",
            "/proc",
            "/root",
            "/sbin",
            "/selinux",
            "/srv",
            "/sys",
            "/usr",
            "/var",
        ]

        # checking directory + hashing it
        if not file_exist(txt_file, txt_path, txt_path_):
            exist = False
            print("Hash file existing : [", bcolors.RED, "-", bcolors.WHITE, "]")
        else:
            print("Hash file existing : [", bcolors.GREEN, "+", bcolors.WHITE, "]")
            exist = True
        for i in range(len(dirs)):
            print("\r\n Checking directory ", dirs[i], end="\r")
            if os.path.exists(str(dirs[i])):
                print(" Checking directory ", dirs[i], " :   ", bcolors.GREEN, "done", bcolors.WHITE, end="\r")

                """
                for files, dirs_ in os.walk(dirs[i]):
                    # hashes of files from a path
                    try:
                        for file in files:
                            sh = hashlib.sha256()
                            print(file)
                            with open(file, "rb") as f:
                                for byte_block in iter(lambda: f.read(4096), b""):
                                    sh.update(byte_block)
                            hashlist[file_n] = sh.hexdigest()
                            file_n += 1
                    except IsADirectoryError:
                        for files_, dirs__ in dirs_:
                            try:
                """
                # extracting one hash from all file hashes
                try:
                    size = get_size(dirs[i])
                    if size > 0:
                        hash_string = str(size)
                        hash_str = encrypt_string(hash_string)
                        for x in range(20):
                            hash_str = encrypt_string(hash_str)
                        print("\r\n Created hash from  ", dirs[i], " : ", bcolors.GREEN, "  done            ",
                              bcolors.WHITE, hash_str)
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
                            print(" Comparing hashes   ", dirs[i], " : ", bcolors.GREEN, "verified", bcolors.WHITE)
                        else:
                            print(" Comparing hashes   ", dirs[i], " : ", bcolors.RED, "unverified        ",
                                  bcolors.WHITE, single_hash[i])
                        digit1 += 64
                        digit2 += 64

                    else:
                        print(bcolors.YELLOW, "\r\n WARNING : creating specific hash failed (empty directory)",
                              bcolors.WHITE)
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
                            print(" Comparing hashes   ", dirs[i], " : ", bcolors.GREEN, "verified", bcolors.WHITE)
                        else:
                            print(" Comparing hashes   ", dirs[i], " : ", bcolors.RED, "unverified          ",
                                  bcolors.WHITE, single_hash[i])
                        digit1 += 64
                        digit2 += 64
                except FileNotFoundError:
                    print(bcolors.RED, "\r\n FATAL ERROR : creating hash failed (empty directory)", bcolors.WHITE)
                    pass
                except PermissionError:
                    print(bcolors.RED, "\r\n FATAL ERROR: permission denied")
                    pass

            else:
                failed = "failed"
                print(" Checking directory ", dirs[i], " ... ", bcolors.RED + failed + bcolors.WHITE)

    hashing()
    print("\r\n\r\nChecking integrity ...", bcolors.GREEN, "done", bcolors.WHITE, "\r\n")


try:
    main()

except KeyboardInterrupt:
    print("\r\nscript shut down...")
    sys.exit()















