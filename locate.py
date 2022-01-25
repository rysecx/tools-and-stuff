#!/usr/bin/python3
# locate script
import os 
import sys

class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'

def find_name(inpName):
    result = ''
    found = False
    for path, dirs, files in os.walk('/'):
            for name in dirs:
                if inpName == name:
                    result = os.path.join(path, inpName)
                    print(f'located: {colors.YELLOW + result + colors.WHITE}')
                    found = True
            for name in files:
                if inpName == name: 
                    result = os.path.join(path, inpName)
                    print(f'located: {colors.YELLOW + result + colors.WHITE}')
                    found = True
    if not found:
        print(f'no match for {colors.RED + inpName + colors.WHITE}')
    else:
        pass

def main():
    inpName = sys.argv[1]
    print(f'searching for {inpName}...')
    find_name(inpName)


if len(sys.argv) == 1 or sys.argv[1] in ('-h', '-help', '--help', '--h'):
	print('usage: ./locate.py [INPUT]')

else:
    try:
        main()
    except Exception as error:
        sys.exit(error)