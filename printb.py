#!/bin/python3
# prints a file in bytemode
import sys
import os

def check_dir(dirPath):
    dirPath = str(dirPath)
    if os.path.exists(str(dirPath)):
        pass
    else:
        print(f'ERROR: File {dirPath} not exists. quitting')
        sys.exit()

def main():
    check_dir(sys.argv(1))
    with open (sys.argv(1), 'rb') as byteFile:
        fileBytes = byteFile.read()
    byteFile.close()
    print(fileBytes)


	
if len(sys.argv) == 1 or sys.argv[1] in ('-h', '-help', '--help', '--h'):
	print('usage: ./printb.py [FILE]')
   
else:
    try:
        main()
    except Exception as error:
        sys.exit(error)
