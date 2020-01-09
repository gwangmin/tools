'''
This script provides image read, write, and display.

img format: bgr, channels last, ndarray
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

def imread(path, flag='c'):
    '''
    Read the image

    path: image file path
    flag: 'c', 'color', 'gray', 'alpha'
    '''
    if flag == 'c' or flag == 'color':
        f = cv2.IMREAD_COLOR
    elif flag == 'gray':
        f = cv2.IMREAD_GRAYSCALE
    elif flag == 'alpha':
        f = cv2.IMREAD_UNCHANGED
    return cv2.imread(path, f)

def show_single(title, img):
    '''
    Show single image
    '''
    return cv2.imshow(title, img)

def show_multi(rows, cols, imgs, names=None):
    '''
    Show images

    rows, cols: space to be showed images
    imgs: matched length with above
    names: img's name
    '''
    for i in range(len(imgs)):
        plt.subplot(rows, cols, i+1)
        b,g,r = cv2.split(imgs[i])
        img = cv2.merge([r,g,b])
        plt.imshow(img)
        if names == None:
            plt.title('img '+str(i))
        else:
            plt.title(names[i])
        plt.xticks([])
        plt.yticks([])
    plt.tight_layout()
    plt.show()

def imwrite(path, img):
    return cv2.imwrite(path, img)


if __name__ == '__main__':
    logo = imread('logo.png')
    show_multi(2,1,[logo,logo])
