from matplotlib import pyplot as plt
import random as r


def plot_resource_util():
    fig1 = plt.figure('Resource Utilization')
    x = [0, 5]
    olive = [1, 1]
    red = [2, 2]

    fig1 = plt.grid(True, color='k')
    fig1 = plt.plot(olive, linewidth=5, label='olive', color='olive')
    fig1 = plt.plot(red, linewidth=5, label='red', color='red')
    fig1 = plt.plot([3, 3], linewidth=5, label='green', color='g')
    fig1 = plt.plot([4, 4], linewidth=5, label='cyan', color='c')
    fig1 = plt.plot([5, 5], linewidth=5, label='blue', color='b')
    fig1 = plt.plot([6, 6], linewidth=5, label='pink', color='pink')
    fig1 = plt.plot([7, 7], linewidth=5, label='magenta', color='m')
    fig1 = plt.plot([8, 8], linewidth=5, label='yellow', color='y')
    fig1 = plt.plot([9, 9], linewidth=5, label='grey', color='grey')
    fig1 = plt.plot([10, 10], linewidth=5, label='brown', color='brown')
    fig1 = plt.plot([11, 11], linewidth=5, label='purple', color='purple')
    fig1 = plt.plot([12, 12], linewidth=5, label='orange', color='orange')
    fig1 = plt.plot([13, 13], linewidth=5, label='burlywood', color='burlywood')
    fig1 = plt.plot([14, 14], linewidth=5, label='chartreuse', color='chartreuse')
    fig1 = plt.plot([15, 15], linewidth=5, label='navy', color='navy')
    fig1 = plt.plot([16, 16], linewidth=5, label='lime', color='lime')
    fig1 = plt.plot([17, 17], linewidth=5, label='aqua', color='aqua')
    fig1 = plt.plot([18, 18], linewidth=5, label='teal', color='teal')
    fig1 = plt.plot([19, 19], linewidth=5, label='fuchsia', color='fuchsia')
    fig1 = plt.plot([20, 20], linewidth=5, label='maroon', color='maroon')
    fig1 = plt.plot([21, 21], linewidth=5, label='silver', color='silver')
    fig1 = plt.title('CPU and RTT Utilization over Time')
    fig1 = plt.ylabel('CPU and RTT')
    fig1 = plt.xlabel('Time (seconds)')
    fig1 = plt.legend()
    plt.show()

plot_resource_util()