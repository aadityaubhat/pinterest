__author__ = 'aaditya'

import gzip,marshal
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import math

def read_data():
    """
    Read data from the data/data.gz
    Arrange the data in a dictionary, with board name being the key and users being the values.
    #for test purpose, only a subset of users being considered
    :return: dictionary of board and users
    """
    data = defaultdict(list)
    with gzip.open('data/data.gz') as file:
        for i,line in enumerate(file):
            #remove if loop to read all the users
            if line.startswith('ab'):
                username , boardname = line.strip().split('\t')
                data[username].append(boardname)
    return data

def store():
    data = read_data()
    fh = gzip.open("processed.gz",'w')
    for k,v in data.iteritems():
        fh.write(k+'\t'+'\t'.join(v)+'\n')
    fh.close()

def hist(data):
    count = defaultdict(int)
    for boards in data.itervalues():
        for b in boards:
            count[b] += 1
    return count

def plot_hist(data):
    counts = hist(data)
    plt.hist(np.asarray([math.log10(counts[i]) for i in counts]), bins = 100)

def top_100_boards(data):
    counts = hist(data)
    top = sorted([(v,k) for k,v in counts.iteritems()],reverse=True)[:100]

def plot_top_100(data):
    top = top_100_boards(data)
    plt.figure(num=None, figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.bar(np.arange(len([i[1] for i in top])*6, step = 6),[i[0] for i in top], width = 6)
    plt.title('Top  100 boards')
    plt.xticks(np.arange(len([i[1] for i in top])*6,step = 6), [i[1] for i in top], rotation= 'vertical', ha = 'left')
    plt.show()




if __name__ == '__main__':
    pass