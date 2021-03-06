# this is a stable version of LFU, LRU and co-operative caching algorithm with gui and real time graphical results
# this is a caching project developed by Emeka

import sqlite3
import hashlib
import os
import socket
import paramiko
from time import gmtime, strftime
import random
import time
import psutil
import ping_code as pc
from drawnow import *
from matplotlib import pyplot as plt
import subprocess as sp
import ast
from pyfiglet import Figlet


__author__ = 'Emeka'
cache_size = 4
H = 0  # hit counter
M = 0  # miss counter
MH = 0  # cooperative hit counter
re_use = 0  # replacement algorithm use counter
ref = [5, 0, 5, 3, 6, 0, 4, 1, 3, 5, 5, 6, 0, 5, 5, 2, 6, 5, 2, 6, 4, 1, 4, 4, 5, 6, 0, 3, 2, 6]
# ref = [14, 14, 7, 0, 15, 15, 5, 18, 7, 14, 8, 17, 10, 14, 10, 16, 17, 12, 16, 0, 4, 10, 1, 12, 4, 5, 7, 6, 14, 19, 18, 7, 10, 19, 5, 13, 8, 14, 10, 16, 10, 0, 0, 13, 2, 4, 9, 17, 14, 10, 10, 5, 19, 11, 0, 16, 8, 10, 19, 8, 8, 18, 13, 16, 16, 10, 7, 11, 15, 6, 19, 7, 6, 1, 10, 15, 1, 14, 13, 4, 5, 5, 9, 2, 5, 6, 14, 15, 11, 15, 7, 0, 4, 7, 0, 12, 7, 10, 13, 6, 16, 7, 14, 17, 6, 0, 12, 11, 12, 15, 12, 16, 9, 7, 13, 12, 10, 11, 9, 4, 6, 2, 15, 15, 3, 7, 15, 19, 4, 7, 14, 14, 0, 12, 4, 13, 14, 6, 7, 16, 6, 4, 16, 3, 15, 15, 9, 1, 5, 7, 15, 17, 4, 1, 15, 17, 18, 17, 5, 0, 16, 11, 10, 14, 6, 18, 5, 4, 17, 1, 15, 4, 10, 19, 19, 2, 7, 4, 3, 8, 15, 1, 2, 9, 8, 10, 17, 1, 12, 3, 2, 11, 14, 19, 16, 19, 4, 6, 13, 12, 13, 12, 3, 10, 7, 13, 12, 12, 8, 3, 3, 4, 7, 5, 7, 2, 0, 16, 1, 2, 7, 12, 10, 8, 16, 3, 10, 17, 11, 8, 10, 1, 18, 10, 0, 11, 12, 18, 8, 13, 6, 19, 0, 12, 18, 10, 9, 8, 10, 4, 1, 10, 15, 16, 11, 12, 6, 0, 12, 14, 18, 7, 1, 12, 4, 19, 0, 17, 3, 17, 7, 15, 3, 14, 6, 12, 6, 12, 19, 0, 10, 17, 14, 5, 9, 17, 18, 14, 6, 19, 9, 12, 12, 7, 0, 6, 11, 1, 7, 15, 4, 9, 14, 18, 10, 5, 15, 18, 11, 7, 19, 4, 11, 13, 4, 12, 1, 5, 5, 7, 9, 4, 18, 14, 4, 11, 5, 13, 5, 4, 13, 15, 15, 0, 1, 1, 14, 14, 6, 18, 9, 14, 15, 1, 5, 3, 17, 6, 0, 8, 9, 13, 13, 1, 4, 7, 10, 0, 12, 16, 18, 3, 1, 1, 18, 6, 1, 10, 8, 13, 16, 6, 15, 8, 2, 1, 10, 4, 7, 11, 13, 7, 9, 12, 9, 11, 10, 8, 11, 0, 3, 3, 14, 8, 15, 1, 15, 11, 19, 15, 14, 13, 5, 1, 16, 3, 17, 18, 16, 15, 13, 0, 11, 6, 10, 18, 16, 18, 6, 7, 16, 13, 6, 2, 0, 6, 6, 2, 9, 4, 12, 9, 10, 11, 18, 6, 11, 19, 14, 9, 9, 5, 8, 6, 1, 6, 19, 15, 7, 1, 9, 5, 13, 6, 12, 13, 19, 8, 14, 9, 0, 13, 8, 7, 13, 11, 11, 12, 8, 9, 3, 12, 7, 1, 4, 8, 6, 5, 17, 7, 19, 4, 18, 16, 4, 9, 8, 9, 4, 6, 7, 19, 18, 4, 12, 13, 11, 4, 19, 6]
#ref = [14, 14, 7, 15, 15, 15, 5, 18, 7, 14, 8, 7, 10, 14, 10, 16, 7, 16, 12, 0, 4, 10, 1, 12, 4, 5, 7, 6, 14, 7, 18, 7, 10, 19, 5, 13, 8, 14, 10, 16, 10, 0, 0, 13, 7, 4, 9, 17, 14, 10, 10, 5, 19, 11, 0, 16, 8, 10, 19, 8, 8, 18, 13, 16, 16, 10, 7, 11, 15, 6, 7, 7, 6, 1, 10, 15, 1, 14, 13, 4, 5, 5, 9, 2, 5, 6, 6, 15, 11, 15, 7, 0, 4, 7, 0, 12, 7, 10, 13, 6, 16, 7, 14, 17, 6, 0, 12, 11, 12, 15, 12, 16, 9, 7, 13, 12, 10, 11, 9, 4, 6, 2, 15, 15, 7, 7, 15, 19, 4, 7, 14, 14, 0, 12, 4, 13, 14, 6, 7, 16, 6, 4, 16, 6, 15, 15, 9, 1, 5, 7, 7, 17, 4, 1, 15, 17, 18, 17, 6, 0, 6, 11, 10, 14, 6, 18, 5, 4, 17, 1, 15, 4, 10, 19, 19, 2, 7, 4, 7, 8, 15, 1, 2, 9, 8, 10, 17, 6, 6, 3, 6, 11, 14, 19, 16, 19, 4, 6, 13, 12, 13, 12, 3, 10, 7, 13, 12, 12, 8, 7, 7, 4, 7, 5, 7, 2, 0, 16, 1, 2, 7, 12, 10, 8, 16, 3, 10, 17, 11, 8, 10, 1, 18, 10, 10, 11, 12, 18, 8, 13, 6, 19, 0, 12, 18, 10, 9, 8, 10, 4, 1, 10, 15, 16, 11, 12, 6, 0, 12, 14, 18, 7, 1, 12, 4, 19, 0, 17, 3, 17, 7, 15, 3, 14, 6, 12, 6, 12, 19, 0, 10, 17, 14, 5, 9, 17, 18, 14, 6, 19, 9, 12, 12, 7, 0, 6, 11, 1, 7, 15, 4, 9, 14, 18, 10, 5, 15, 18, 11, 7, 19, 4, 11, 13, 4, 12, 1, 5, 5, 7, 9, 4, 18, 14, 4, 11, 5, 13, 5, 4, 13, 15, 15, 0, 1, 1, 14, 14, 6, 6, 9, 14, 15, 15, 5, 3, 15, 6, 0, 8, 13, 13, 13, 1, 4, 7, 10, 0, 12, 16, 18, 3, 1, 1, 18, 6, 1, 10, 8, 13, 16, 6, 15, 8, 15, 1, 10, 4, 7, 11, 13, 7, 9, 12, 9, 11, 10, 8, 11, 0, 11, 3, 14, 8, 15, 1, 15, 11, 19, 15, 14, 13, 5, 1, 16, 3, 17, 18, 16, 15, 13, 0, 11, 6, 10, 18, 16, 18, 6, 7, 16, 13, 6, 2, 0, 6, 6, 6, 9, 4, 12, 9, 10, 11, 18, 6, 11, 19, 14, 9, 9, 5, 8, 6, 1, 6, 19, 15, 7, 1, 9, 5, 13, 6, 12, 13, 19, 8, 14, 9, 0, 13, 8, 7, 13, 11, 11, 12, 8, 9, 3, 12, 7, 1, 4, 8, 6, 5, 17, 7, 19, 4, 18, 16, 4, 9, 8, 9, 4, 6, 7, 19, 18, 4, 12, 13, 11, 4, 19, 6]


color_code = ['r', 'g', 'c', 'b', 'm', 'y', 'grey', 'pink', 'brown', 'purple', 'orange', 'burlywood', 'lime', 'navy', 'aqua', 'teal', 'fuchsia', 'olive', 'maroon', 'silver']

freq = {}
changing_freq = {}  # {hash: frequency}
window_size = 0

x_axis = []
y_axis = []

fig = plt.figure()
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(233)
ax3 = fig.add_subplot(234)
ax4 = fig.add_subplot(236)
ax5 = fig.add_subplot(132)


def make_hash_dic(host_ip, n):
    global hash_colour
    global hash_web

    h_dic = {}   # {url: hash}
    kolour = color_code[:n]
    col = {}     # {url: colour}
    hash_colour = {}     # {hash: colour}
    hash_web = {}   # {hash: url}
    for i in range(1, n+1):
        url = '{}/{}.html'.format(host_ip, i)
        hash_me = 'get {} HTTP/1.0'.format(url)
        y = str.encode(hash_me)
        ha = hashlib.md5(y)
        hash_no = ha.hexdigest()
        hash_colour[hash_no] = kolour[i-1]
        hash_web[hash_no] = url
        h_dic[url] = hash_no
        col[url] = kolour[i-1]
    return [h_dic, col]


def plot_performance():
    global H
    global M
    global MH
    global re_use

    name = ['Hit', 'Miss', 'CH', 'AU']
    ypos = ([0, 1, 2, 3])
    values = [H, M, (H + MH), re_use]
    ax1.set_xticks(ypos)
    ax1.set_xticklabels(name)
    ax1.bar(ypos, values, align='center', color='m')
    ax1.set_title('Cache Performance')
    plt.subplot(ax1)


def update_changing_freq():
    for key in freq.keys():
        x = key
        y = freq[key]
        if x in changing_freq.keys():
            changing_freq[x].append(y)
        else:
            changing_freq[x] = [y]


def plot_changing_freq():
    global changing_freq

    '''
    plot_dic = {}

    for key in hash_dic:
        if hash_dic[key] not in changing_freq:
            continue
        elif hash_dic[key] in changing_freq:
            rf = changing_freq[hash_dic[key]]
            plot_dic[key] = rf  # converts the dictionary from hash: frequency to web: frequency

    ax2.grid(True, color='k')
    for key in plot_dic.keys():
        ax2.plot(plot_dic[key], linewidth=5, label=key.split('/')[1], color=colour[key])
    '''
    ax2.grid(True, color='k')
    for key in changing_freq.keys():
        ax2.plot(changing_freq[key], linewidth=5, label=hash_web[key].split('/')[1], color=hash_colour[key])

    ax2.set_title('Changing frequency Graph')
    ax2.set_ylabel('URL')
    ax2.set_xlabel('Time (seconds)')
    ax2.legend()
    plt.subplot(ax2)


def local_cache_frequency():
    ip = ip_address()

    con = sqlite3.connect('/home/mec/cache.db')
    cur = con.cursor()
    cur.execute("select Hash from CacheTable where Host_ip ='" + ip + "'")
    data = cur.fetchall()
    '''
    data format
    [('7e7ea8d98195d1fcf6abe4f77e56730e',), ('26ff04f8463191809dcd9e8605bb952a',), ('d37269610dffb86e4925864b110e4d4e',)]
    '''
    d = []
    if len(data) == 0:
        con.close()
        return 'no items'
        pass
    else:
        for i in data:
            d.append(i[
                         0])  # cleaning data to d = ['7e7ea8d98195d1fcf6abe4f77e56730e', '26ff04f8463191809dcd9e8605bb952a', 'd37269610dffb86e4925864b110e4d4e']
        con.close()
        cache_dic = {}   # {hash: relative frequency}
        for i in d:
            cache_dic[i] = freq[i]  # creates a dictionary and tags the hash with its relative frequency

        plot_dic = {}   # {url: relative frequency}

        for key in hash_dic:
            if hash_dic[key] not in cache_dic:
                continue
            elif hash_dic[key] in cache_dic:
                rf = cache_dic[hash_dic[key]]
                plot_dic[key] = rf  # converts the dictionary from hash: frequency to web: frequency

        return plot_dic


def plot_local_cache_freq():
    global changing_freq

    plot_dic = {}

    for key in hash_dic:
        if hash_dic[key] not in changing_freq:
            continue
        elif hash_dic[key] in changing_freq:
            rf = changing_freq[hash_dic[key]]
            plot_dic[key] = rf  # converts the dictionary from hash: frequency to web: frequency

    ax3.grid(True, color='k')
    if local_cache_frequency() == 'no items':
        pass
    else:
        for key in plot_dic.keys():
            if key in local_cache_frequency():
                ax3.plot(plot_dic[key], linewidth=5, label=key.split('/')[1], color=colour[key])

        ax3.set_title('Local Cache frequency Graph')
        ax3.set_ylabel('URL')
        ax3.set_xlabel('Time (seconds)')
        ax3.legend()
        plt.subplot(ax3)


def hash_to_web():
    global freq

    plot_dic = {}

    for key in hash_dic:
        if hash_dic[key] not in freq:
            continue
        elif hash_dic[key] in freq:
            rf = freq[hash_dic[key]]
            plot_dic[key] = rf

    return plot_dic


def plot_graphs():
    plot_resource_util()
    plot_relative_frequency()
    plot_changing_freq()
    plot_local_cache_freq()
    plot_performance()
    fig.suptitle('Cache Performance Results')


def cpu_rtt():
    host = server_ip
    prev_t = 0
    rtt = pc.verbose_ping(host)
    next_t = psutil.cpu_percent(percpu=False)
    delta = abs(prev_t - next_t)
    prev_t = next_t
    x_axis.append(rtt)
    y_axis.append(delta)


def calculate_mov_avg(a1):
    ma1=[] # moving average list
    avg1=0 # movinf average pointwise
    count=0
    for i in range(len(a1)):
        count+=1
        avg1=((count-1)*avg1+a1[i])/count
        ma1.append(avg1) #cumulative average formula
    return ma1


def plot_resource_util():
    ax4.grid(True, color='k')
    ax4.plot(calculate_mov_avg(x_axis), linewidth=5, label='RTT')
    ax4.plot(calculate_mov_avg(y_axis), linewidth=5, label='CPU')
    ax4.set_title('CPU and RTT Utilization over Time')
    ax4.set_ylabel('CPU and RTT')
    ax4.set_xlabel('Time (seconds)')
    ax4.legend()
    plt.subplot(ax4)


def plot_relative_frequency():
    ret = hash_to_web()

    val = []
    keys = []
    cols = []

    for i in ret.items():
        val.append(i[1])
        keys.append(i[0].split('/')[1])
        cols.append(hash_colour[i[0]])

    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax5.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax5.set_title('Relative Frequency')
    plt.subplot(ax5)


def get_hash(url):
    hash_me = 'get {} HTTP/1.0'.format(url)
    y = str.encode(hash_me)
    ha = hashlib.md5(y)
    hash_no = ha.hexdigest()
    calc_relative_freq(hash_no)
    check_cache(hash_no, url)


def calc_relative_freq(x):
    global freq
    global window_size

    window_size += 1
    alpha = 1 / window_size
    delta = alpha / (len(freq) + 1)
    if x not in freq.keys():
        for k in freq.keys():
            freq[k] -= delta
        freq[x] = alpha
    else:
        for k in freq.keys():
            if k != x:
                freq[k] -= delta
        freq[x] += (len(freq) - 1) * delta

    update_changing_freq()
    cpu_rtt()
    drawnow(plot_graphs)


def get_time():
    y = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return y


def ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def check_cache(hash_no, url):
    try:
        global con
        con = sqlite3.connect('/home/mec/cache.db')
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM CacheTable WHERE Hash='" + hash_no + "'")
        d = cur.fetchone()
        r = d[0]
        if r == 0:
            fetch_from_source(hash_no, url)
        else:
            fetch_from_cache(hash_no)

    except sqlite3.Error as e:
        if con:
            con.rollback()
            print('Error in check_cache: {}'.format(e))

    finally:
        if con:
            con.close()


def fetch_from_source(hash_no, url):
    global M
    cmd = "curl {}".format(url)
    os.system(cmd)

    prepare_db()  # CHECKS IF CACHE IS FULL AND ELIMINATES VICTIM

    cmd = "echo `curl {}` > /home/mec/cache/{}.html".format(url, hash_no)  # CACHES DATA FROM SOURCE
    os.system(cmd)
    print('-----------------------------------')
    print('Cache Miss')
    print('-----------------------------------')
    M += 1
    update_local_database(hash_no)


def update_local_database(hash_no):
    try:
        global con

        con = sqlite3.connect('/home/mec/cache.db')
        cur = con.cursor()
        cache_time = get_time()
        ip = mec_me['ip']
        path = '/home/mec/cache/{}.html'.format(hash_no)
        data = (hash_no, path, cache_time, ip)
        cur.execute("INSERT INTO CacheTable VALUES(?, ?, ?, ?)", data)
        con.commit()
        cur.execute("SELECT * FROM CacheTable")
        d = cur.fetchall()

        for row in d:
            print(row)

        update_mec_database(hash_no, path, cache_time, ip)
        con.close()

    except sqlite3.Error as e:
        print('Error in cache_update: {}'.format(e))


def update_mec_database(hash_no, path, cache_time, host_ip):
    for i in mec_list:
        c = paramiko.SSHClient()

        un = 'mec'
        pw = 'password'
        port = 22

        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(mec_list[i], port, un, pw)
        cmd = 'python3 /home/mec/files_cache/db_manage.py insert "{}" "{}" "{}" "{}"'.format(hash_no, path, cache_time, host_ip)

        stdin, stdout, stderr = c.exec_command(cmd)


def fetch_from_cache(hash_no):
    try:
        global con
        global H
        con = sqlite3.connect('/home/mec/cache.db')
        cur = con.cursor()
        cur.execute("SELECT Host_ip FROM CacheTable WHERE Hash='" + hash_no + "'")
        host_ip_list = cur.fetchall()
        h_list = []
        for i in host_ip_list:
            h_list.append(i[0])

        local_ip = ip_address()
        if local_ip in h_list:
            time = get_time()
            cmd = "cat /home/mec/cache/{}.html".format(hash_no)
            os.system(cmd)
            print('-----------------------------------')
            print('Cache Hit from localhost')
            print('-----------------------------------')
            H += 1
            cur.execute(
                "update CacheTable set DateTime = '" + time + "' where Hash = '" + hash_no + "' and Host_ip = '" + local_ip + "';")
            con.close()
        elif len(host_ip_list) == 1:
            fetch_from_mec(hash_no, host_ip_list[0][0])

        elif len(host_ip_list) > 1:
            max_band_ip = h_list[random.randint(0, len(h_list)-1)]
            fetch_from_mec(hash_no, max_band_ip)

    except sqlite3.Error as e:
        print('Error in cache_update: {}'.format(e))


def frequently_used(hash_no):
    host_ip = mec_me['ip']
    global freq
    try:
        global con
        con = sqlite3.connect('/home/mec/cache.db')
        cur = con.cursor()
        cur.execute("SELECT Hash FROM CacheTable WHERE Host_ip ='" + host_ip + "'")
        host_ip_list = cur.fetchall()
        con.close()
        li = []
        for i in range(len(host_ip_list)):
            li.append(host_ip_list[i - 1][0])
        fre_li = []
        for i in li:
            fre_li.append(freq[i])
        min_freq = min(fre_li)

        if min_freq > freq[hash_no]:
            return 'no'
        elif min_freq < freq[hash_no]:
            y = fre_li.index(min_freq)
            delete_least_frequent_mec(li[y], host_ip)
            delete_least_frequent_locally(li[y], host_ip)
            return 'yes'

    except sqlite3.Error as e:
        print('Error in cache_update: {}'.format(e))


def delete_least_frequent_locally(hash_no, host_ip):
    try:
        con = sqlite3.connect('/home/mec/cache.db')
        cur = con.cursor()
        cur.execute("DELETE FROM CacheTable WHERE Hash = '" + hash_no + "' AND Host_ip = '" + host_ip + "'")
        con.commit()
        con.close()
        cmd = 'rm /home/mec/cache/{}.html'.format(hash_no)
        os.system(cmd)

    except sqlite3.Error as e:
        print('Error in cache_update: {}'.format(e))


def delete_least_frequent_mec(hash_no, host_ip):
    for i in mec_list:
        c = paramiko.SSHClient()

        un = 'mec'
        pw = 'password'
        port = 22

        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(mec_list[i], port, un, pw)
        cmd = 'python3 /home/mec/files_cache/db_manage.py del "{}" "{}" '.format(hash_no, host_ip)

        stdin, stdout, stderr = c.exec_command(cmd)


def fetch_from_mec(hash_no, host_ip):
    c = paramiko.SSHClient()
    global MH
    global re_use

    un = 'mec'
    pw = 'password'
    port = 22

    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(host_ip, port, un, pw)
    cmd = 'cat /home/mec/cache/{}.html'.format(hash_no)

    stdin, stdout, stderr = c.exec_command(cmd)

    con = sqlite3.connect('/home/mec/cache.db')
    cur = con.cursor()

    ip = mec_me['ip']

    cur.execute("SELECT COUNT(*) FROM CacheTable WHERE Host_ip='" + ip + "'")
    d = cur.fetchone()
    r = d[0]  # This value represents how many data entries for host_ip

    if r >= cache_size and frequently_used(hash_no) == 'no':
        for line in stdout:
            q = len(line) - 1
            t = line[:q]
            print(t)
        print('-----------------------------------')
        print('Hit from MEC Not Cached')
        print('-----------------------------------')
        MH += 1
    else:
        for line in stdout:
            q = len(line) - 1
            t = line[:q]
            cmd = "echo '{}' >> /home/mec/cache/{}.html".format(t, hash_no)
            os.system(cmd)
        cmd = 'cat /home/mec/cache/{}.html'.format(hash_no)
        update_local_database(hash_no)
        os.system(cmd)
        print('-----------------------------------')
        print('Cache Hit from MEC')
        print('-----------------------------------')
        MH += 1
        if r >= cache_size:
            re_use += 1
    con.close()


'''
def get_max_band():
    M1 = '10.1.1.1'
    M2 = '10.2.2.2'
    # M3 = '10.3.3.3'
    conn = sqlite3.connect('/home/mec/cache.db')
    curr = conn.cursor()
    sql_cmd = "SELECT M1, M2 FROM Bw_Table ORDER BY Id DESC LIMIT 1;"
    curr.execute(sql_cmd)
    data = curr.fetchone()
    a = data[0]
    b = data[1]
    c = [a, b]
    d = max(c)
    e = c.index(d)
    if e == 0:
        return M1
    elif e == 1:
        return M2
'''


def prepare_db():
    global re_use

    host_ip = mec_me['ip']
    try:
        con = sqlite3.connect('/home/mec/cache.db')
        cur = con.cursor()

        cur.execute("SELECT COUNT(*) FROM CacheTable WHERE Host_ip='" + host_ip + "'")
        d = cur.fetchone()
        r = d[0]  # This value represents how many data entries for host_ip
        if r >= cache_size:
            cur.execute("SELECT DateTime FROM CacheTable where Host_ip = '" + host_ip + "'")

            data = cur.fetchall()  # returns array that looks like [('2018-08-20 13:23:49',), ('2018-08-20 11:56:04',), ('2018-08-20 13:40:01',)]

            min_time = min(data)[0]  # Return minimum time

            delete_from_mec(min_time, host_ip)

            cur.execute(
                "SELECT Hash FROM CacheTable WHERE DateTime = '" + min_time + "' AND Host_ip = '" + host_ip + "'")
            data = cur.fetchone()

            cmd = 'rm /home/mec/cache/{}.html'.format(data[0])
            os.system(cmd)

            cur.execute("DELETE FROM CacheTable WHERE DateTime = '" + min_time + "' AND Host_ip = '" + host_ip + "'")
            con.commit()
            con.close()
            re_use += 1

            # cur.execute("SELECT * FROM CacheTable")

    except sqlite3.Error as e:
        print('Error Encountered: {}'.format(e))


def delete_from_mec(min_time, host_ip):
    for i in mec_list:

        c = paramiko.SSHClient()

        un = 'mec'
        pw = 'password'
        port = 22

        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(mec_list[i], port, un, pw)
        cmd = 'python3 /home/mec/files_cache/db_manage.py delete "{}" "{}" '.format(min_time, host_ip)

        stdin, stdout, stderr = c.exec_command(cmd)


def cache_performance():
    global H
    global M
    global MH
    global window_size
    global re_use
    p = int((H / request_no) * 100)
    q = int(((H+MH) / request_no) * 100)
    print('----------------------------------------------------------')
    print('                   Cache Performance')
    print('----------------------------------------------------------')
    print('local MEC Performance: {}% | Cooperative Performance: {}% '.format(p, q))
    print('\nLocal Cache hits: {}       | Cache Misses: {}'.format(H, M))
    print('\nMEC Cache hits: {}         | Total Cache hits: {}'.format(MH, H + MH))
    print('----------------------------------------------------------')
    print('         Total use of Replacement Algorithm = {}'.format(re_use))
    print('----------------------------------------------------------')
    cmd = "echo 'lfru{}_local_hits = {} \nlfru{}_miss = {} \nlfru{}_mec_hit = {} \n" \
          "lfru{}_total_hit = {}' >> /home/mec/cache_result.py".format(cache_size, H, cache_size, M, cache_size, MH, cache_size, H+MH)
    os.system(cmd)


def getting_ready():
    global mec_me  # {'hostname': <hostname>, 'ip': <ip>}

    my_ip = ip_address()

    cmd = ['cat /etc/hostname | cut -c 1-4']
    hostname = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
    print('hostname = {}'.format(hostname))

    cmd = ['netstat -nr | head -n 3 | tail -n 1 | cut -d " " -f 10']
    router_ip = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
    print('router_ip = {}'.format(router_ip))

    mec_me = {'hostname': hostname, 'ip': my_ip}

    cmd = "bash /home/mec/files_cache/hosts.sh {}/24 > /home/mec/temp/names.txt".format(router_ip)

    os.system(cmd)
    mec_set = {my_ip, router_ip}
    fr = open('/home/mec/temp/names.txt', 'r')

    ips = []
    f1 = fr.readlines()
    for i in f1:
        ips.append(i[0:-1])

    fr.close()

    available_host = set(ips) - mec_set

    for i in available_host:
        try:
            c = paramiko.SSHClient()

            un = 'mec'
            pw = 'password'
            port = 22

            c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            c.connect(i, port, un, pw)
            cmd = ('echo "' + "'{}' : '{}'".format(hostname, my_ip) + '" >> /home/mec/temp/mec_list.txt')

            stdin, stdout, stderr = c.exec_command(cmd)
        except:
            print('connecting. . .')
            print('make sure ssh is running on all MEC')


def run_me():
    global hash_dic
    global mec_list  # {'mec1': ip_address, 'mec3': 'ip_address'}
    global server_ip
    global request_no
    global colour

    os.system('clear')
    server_ip = input('web server ip: ')
    n = int(input('number of web(html) contents: '))
    request_no = int(input('number of requests: '))
    for i in range(1, n+1):
        cmd = 'echo "{}/{}.html" >> /home/mec/temp/web_test.txt'.format(server_ip, i)
        os.system(cmd)
    result = make_hash_dic(server_ip, n)
    hash_dic = result[0]
    colour = result[1]
    os.system('clear')

    print("getting ready to start. . .")

    time.sleep(3)
    getting_ready()
    os.system('clear')
    g = Figlet(font='bubble')

    print(g.renderText('MEC CACHING PROJECT'))
    print(g.renderText('                      BY     EMEKA '))

    while True:
        print('\n')
        s = input('Enter any key to start and "stop" to exit: ')
        if s == 'stop':
            print('\nProgramme Terminated')
            print(freq)
            cache_performance()
            os.system('rm /home/mec/temp/*')
            cmd = "echo 'lfru{}_rtt = {} \nlfru{}_cpu = {}' >> /home/mec/cache_result.py".format(cache_size, calculate_mov_avg(x_axis), cache_size, calculate_mov_avg(y_axis))
            os.system(cmd)
            break
        else:
            mec_str = ''
            tr = open('/home/mec/temp/mec_list.txt', 'r')
            tp = tr.readlines()
            for i in tp:
                mec_str += i[0:-1] + ','
            mec = '{' + mec_str[0:-1] + '}'
            mec_list = ast.literal_eval(mec)
            '''
            for i in range(30):
                fr = open('/home/mec/temp/web_test.txt', 'r')
                t = fr.readlines()
                v = random.randint(0, (len(t) - 1))
                get_hash(t[v][0:-1])
                fr.close()
                time.sleep(3)
            '''

            for v in ref:
                fr = open('/home/mec/temp/web_test.txt', 'r')

                t = fr.readlines()
                get_hash(t[v][0:-1])
                fr.close()
                time.sleep(1)


def main():
    run_me()


if __name__ == "__main__":
    main()
