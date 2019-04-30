from matplotlib import pyplot as plt
from drawnow import *
import random as r
import time

fig = plt.figure()
ax1 = fig.add_subplot(331)
ax2 = fig.add_subplot(332)
ax3 = fig.add_subplot(333)
ax4 = fig.add_subplot(334)
ax5 = fig.add_subplot(313)


def plt1():
    x = list(range(10, 30))
    y = [r.randrange(i) for i in x]
    ax1.grid(True, color='k')
    ax1.plot(x, y, linewidth=5, color='g')
    ax1.set_title('plt1')
    ax1.legend()
    plt.subplot(ax1)


def plt2():
    x = list(range(10, 30))
    y = [r.randrange(i) for i in x]
    ax2.grid(True, color='k')
    ax2.plot(x, y, linewidth=5, color='c')
    ax2.set_title('plt1')
    ax2.legend()
    plt.subplot(ax2)


def plt3():
    x = list(range(10, 30))
    y = [r.randrange(i) for i in x]
    ax3.grid(True, color='k')
    ax3.plot(x, y, linewidth=5, color='m')
    ax3.set_title('plt1')
    ax3.legend()
    plt.subplot(ax3)


def plt4():
    x = list(range(10, 30))
    y = [r.randrange(i) for i in x]
    ax4.grid(True, color='k')
    ax4.plot(x, y, linewidth=5, color='k')
    ax4.set_title('plt1')
    ax4.legend()
    plt.subplot(ax4)


def plt5():
    x = list(range(51, 58))
    val = [r.randrange(i) for i in x]
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


def plot_test():

    try:
        plt1()
        plt2()
        plt3()
        plt4()
        plt5()
        fig.suptitle('Testing subplot')
    except Exception as e:
        print(e)


def draw_loop():
    while True:
        drawnow(plot_test)
        time.sleep(3)


draw_loop()
