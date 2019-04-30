from matplotlib import pyplot as plt
from drawnow import *
import random as r


fig = plt.figure()
ax1 = fig.add_subplot(331)
ax2 = fig.add_subplot(332)
ax3 = fig.add_subplot(333)
ax4 = fig.add_subplot(334)
ax5 = fig.add_subplot(313)


def plt1():
    x = list(range(10, 30))
    y = [r.randint(i) for i in x]
    ax1.grid(True, color='k')
    ax1.plot(x, y, linewidth=5, color='g')
    ax1.set_title('plt1')
    ax1.legend()
    plt.subplot(ax1)


def plt2():
    x = list(range(10, 30))
    y = [r.randint(i) for i in x]
    ax1.grid(True, color='k')
    ax1.plot(x, y, linewidth=5, color='c')
    ax1.set_title('plt1')
    ax1.legend()
    plt.subplot(ax1)


def plt3():
    x = list(range(10, 30))
    y = [r.randint(i) for i in x]
    ax1.grid(True, color='k')
    ax1.plot(x, y, linewidth=5, color='m')
    ax1.set_title('plt1')
    ax1.legend()
    plt.subplot(ax1)


def plt4():
    x = list(range(10, 30))
    y = [r.randint(i) for i in x]
    ax1.grid(True, color='k')
    ax1.plot(x, y, linewidth=5, color='k')
    ax1.set_title('plt1')
    ax1.legend()
    plt.subplot(ax1)


def plt5():
    val = [2, 4, 6, 10, 1, 0.5, 15]
    explode = []
    for v in val:
        if v == max(val):
            explode.append(0.1)
        else:
            explode.append(0)
    keys = ['bird', 'car', 'ford', 'eagle', 'snake', 'lion', 'tiger']
    cols = ['r', 'g', 'c', 'k', 'b', 'm', 'y']
    ax5.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax5.set_title('Relative Frequency')