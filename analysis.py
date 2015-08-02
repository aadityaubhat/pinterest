__author__ = 'aaditya'

import gzip
import re
import pandas
import bokeh

pandas.DataFrame
def read_data():
    """
    Read data from the data/data.gz
    Arrange the data in a dictionary, with board name being the key and users being the values.
    #for test purpose, only a subset of users being considered
    :return: dictionary of board and users
    """
    res = {}
    with gzip.open('data/data.gz') as file:
        for line in file:
            #remove if loop to read all the users
            if re.match('^ab[a-z]*[A-Z]*[0-9]*', line):
                if line.split('\t')[1].replace('\n', '') in res:
                    res[line.split('\t')[1].replace('\n', '')].append(line.split('\t')[0])
                else:
                    res[line.split('\t')[1].replace('\n', '')] = []
                    res[line.split('\t')[1].replace('\n', '')].append(line.split('\t')[0])
    return  res

def top_50_boards(board_user):
    top50 = {}
    for i, board in enumerate(board_user):
        if i == 49:
            break
        else:
            top50[i] = [board,len(board_user[board])]
    for board in board_user:
        for i in xrange(len(top50)):
            if len(board_user[board]) > top50[i][1]:
                top50[i] = [board,len(board_user[board])]
                break
    return top50

def hist(board_users):
    hist = {}
    for board in board_users:
        hist[board] = len(board_users[board])
    return hist

if __name__ == '__main__':
    pass