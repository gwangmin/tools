'''
This script removes .pyc/__pycache__ in current directory or sub directory
'''

import os

for path, dirs, files in os.walk('.'):
    for fname in files:
        if fname.find('.pyc') != -1:
            os.system('rm '+path+'/'+fname)
    for dname in dirs:
        if dname == '__pycache__':
            os.system('rm -rf '+path+'/'+dname)

