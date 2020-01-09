'''
matplotlib wrapper
'''

import matplotlib.pylab as plt
import numpy as np

def show():
    '''
    Show plot
    == plt.show()
    '''
    plt.show()

def single_line(x, y, color, marker, linestyle, figsize=None, title='Figure', xticks=None, yticks=None, xlim=None, ylim=None, xlabel='x', ylabel='y', grid=True, legend=None):
    '''
    Draw a line
    
    x: list of x or None
    y: list of y
    color: color name or hex code
    marker: refer to style args
    linestyle: refer to style args
    figsize: figure size. (rows, cols)
    title: title string.
    xticks: list of num or (list of num, list of string)
    yticks: list of num or (list of num, list of string)
    xlim: (x_min, x_max). Show [x_min, x_max]
    ylim: (y_min, y_max). Show [y_min, y_max]
    xlabel: x axis label string
    ylabel: y axis label string
    grid: whether showing grid
    legend: == ple.legend(loc=)
        available value: https://datascienceschool.net/view-notebook/d0b1637803754bb083b5722c9f2209d0/#%EB%B2%94%EB%A1%80

    style args: https://datascienceschool.net/view-notebook/d0b1637803754bb083b5722c9f2209d0/#%EC%8A%A4%ED%83%80%EC%9D%BC-%EC%A7%80%EC%A0%95
    '''
    # figure size
    if figsize != None:
        plt.figure(figsize=(figsize[1], figsize[0]))
    # title
    plt.title(title)
    # plot
    if x == None:
        plt.plot(y, color=color, marker=marker, linestyle=linestyle)
    else:
        plt.plot(x, y, color=color, marker=marker, linestyle=linestyle)
    # ticks
    if xticks != None:
        if isinstance(xticks, list):
            plt.xticks(xticks)
        else:
            plt.xticks(xticks[0], xticks[1])
    if yticks != None:
        if isinstance(yticks, list):
            plt.yticks(yticks)
        else:
            plt.yticks(yticks[0], yticks[1])
    # lim
    if xlim != None:
        plt.xlim(xlim[0], xlim[1])
    if ylim != None:
        plt.ylim(ylim[0], ylim[1])
    # axis label
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # grid
    plt.grid(grid)
    # legend
    if legend != None:
        plt.legend(loc=legend)
    # adjust layout
    plt.tight_layout()


