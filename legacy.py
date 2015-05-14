__author__ = 'aaditya'
import gzip
import config
import entity


def extract_line(line):
    """
    Read a single line and parse it
    Line example: username \t 1,2,3,5:board_name \t ... \n
    :param line:
    :returns a username,list of (boards and list of dates)
    """
    e = line.strip().split('\t')
    username = e[0]
    boards, dates = {}, []  # this is a dictionary,list
    for k in e[1:]:  # for each loop
        date,board = k.split(':')
        boards[board] = date.split(',')
        # dates.append(date)
    # result = [username, boards, dates]
    return username, boards

def hist_boards():
    """
    Compute histogram of board counts, store as a list, max board_count = 20, ignore > 20, for first 100,000 users
    :return:
    """
    pinterest = gzip.open('data/pinterest.gz')
    result = {}
    c = 0
    for line in pinterest:
        u,b = extract_line(line)
        result[u]=b
        c+=1
        if c == 100000:
            break
    pinterest.close()
    resultlist =[]
    for l in result:
        resultlist.append(len(result[l]))
    count = {}
    for m in range(1,21):
        count [m] = resultlist.count(m)
    return count # remove later, understand warning

if __name__ == '__main__':
    hist_boards()
