'''
This script removes .pyc, __pycache__, .DS_Store, .ipynb_checkpoints in current directory or sub directory
in bash
'''

import os
import sys


def remove():
    for path, dirs, files in os.walk('.'):
        for fname in files:
            if ('.pyc' in fname) or ('.DS_Store' in fname):
                os.system('rm '+path+'/'+fname)
        for dname in dirs:
            if (dname == '__pycache__') or (dname == '.ipynb_checkpoints'):
                os.system('rm -rf '+path+'/'+dname)


def main():
    remove()
    print('[*] Removed')


if __name__ == '__main__':
    main()

