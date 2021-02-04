'''
This script changes all src word to dst word.(in current and sub dirs)
More information, please read the help msg 'python change_all_word.py -h'.
'''

import os
import sys


def change_word(fname, src, dst):
    '''
    Change src to dst in file named fname.
    
    fname: file name
    src: name to change
    dst: changed name
    '''
    con = None
    
    with open(fname, 'r') as f:
        con = f.read()
        
    con = con.replace(src, dst)

    with open(fname, 'w') as f:
        f.write(con)


def help_msg():
    '''
    Print this program's help message
    '''
    return 'python ' + sys.argv[0] + ' <src_word> <dst_word>'


def main():
    if sys.argv[1] == '-h':
        print( help_msg() )
        exit(0)
    
    for path,dirs,files in os.walk('.'):
        for fname in files:
            if fname != sys.argv[0]:
                f = path + '/' + fname
                change_word(f, sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
