import unicodedata
import os

def show_dir(dir:str = '.'):
    '''
    Show files NFC/NFD info.

    dir: dir path. default current dir.
    '''
    for fname in os.listdir(dir):
        print(fname)
        print('NFC: ', unicodedata.is_normalized('NFC', fname))
        print('NFD: ', unicodedata.is_normalized('NFD', fname))
        print()

def NFD2NFC_fname(dir:str = '.'):
    '''
    Convert filenames in this dir. NFD -> NFC.

    dir: dir path. default current dir.
    '''
    for fname in os.listdir(dir):
        os.rename(fname, unicodedata.normalize('NFC', fname))

if __name__ == '__main__':
    NFD2NFC_fname()
