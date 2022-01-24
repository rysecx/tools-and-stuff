#!/bin/python3
# script to remove files encrypted and not even readable after restoring
from cryptography.fernet import Fernet
import os
import sys

def check_dir(dirPath):
        if os.path.exists(str(dirPath)):
            pass
        else:
            print(f'ERROR: File {dirPath} not exists. quitting')
            sys.exit()

def encrypt_data(fileData):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encryptedData = fernet.encrypt(fileData)
    return encryptedData

def main():
    file = sys.argv[1]
    check_dir(file)
    with open (file, 'rb') as f:
        fileData = f.read()
    f.close()
    fileData = encrypt_data(fileData)
    with open (file, 'wb') as f:
        f.write(fileData)
    f.close()
    os.remove(file)
    print(f'removed {file} encrypted')


if len(sys.argv) == 1 or sys.argv[1] in ('-h', '-help', '--help', '--h'):
    print('usage: ./rmsf.py [FILE]')

else:
    try:
        main()
    except Exception as error:
        sys.exit(error)
