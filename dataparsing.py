__author__ = 'aaditya'

import xml.etree.ElementTree
import urllib
import gzip
import os
import time
import sys
from db import DB


def parse_link(link):
    """
    check if the file exists or else download;
    :param link: robot.txt url
    :return: a dictionary of gzfiles and dates
    """

    try:
        if not (os.path.isfile('data_aaditya/mainlink.xml')):
            file = urllib.URLopener()
            file.retrieve(link, "data_aaditya/mainlink.xml")
        root = xml.etree.ElementTree.parse("data_aaditya/mainlink.xml").getroot()
        result = {}
        for i in xrange(0,len(root)):
            result[i] = root[i][0].text, root[i][1].text.rsplit('T')[0]
        return result
    except IOError:
        DB['pindb']['error_log'].insert( {"URL" : link})


def parse_gz(sitemap_file):
    """
    check if the file exists or else download;
    unzip the gz file;
    parse the xml file;
    extract the links from xml file;
    :param sitemap_file: a single xml.gz file
    :return: a dictionary of link(consisting of username and boards) & dates
    """
    if not (os.path.isfile(('data_aaditya/'+sitemap_file[0].rsplit('/')[4]))):
        # try:
        file = urllib.URLopener()
        file.retrieve(sitemap_file[0], ('data_aaditya/'+sitemap_file[0].rsplit('/')[4]))
        # except:
        #     DB['pindb']['error_log'].insert( {"FILE" : sitemap_file[0].rsplit('/')[4]})
        #     return {}
    # try:
    f = gzip.open(('data_aaditya/'+sitemap_file[0].rsplit('/')[4]), 'rb')
    root = xml.etree.ElementTree.fromstring(f.read())
    f.close()
    result = {}
    for i in xrange(0,len(root)):
        result[i] = root[i][0].text, sitemap_file[1]
    return result
    # except IOError:
    #     DB['pindb']['error_log'].insert({"GZ File" : sitemap_file[0].rsplit('/')[4]})
    #     return {}



def slicelink(lst):
    """
    :param lst: link containing username and board
    :return: tuple of username, board name & dates
    """
    return lst[0].rsplit('/')[3], lst[0].rsplit('/')[4], lst[1]

def main(fileurl, sysarg):
    linklist = parse_link(fileurl)
    for i in xrange(0,len(linklist)):
        if i%10 == sysarg:
            gzfiles = parse_gz(linklist[i])
            if(len(gzfiles) == 0):
                continue
            docs = []
            for j in xrange(0, len(gzfiles)):
                docs.append({'user' : slicelink(gzfiles[j])[0], 'board' : slicelink(gzfiles[j])[1], 'date' : slicelink(gzfiles[j])[2]})
            DB['pindb']['user_board_date'].insert_many(docs)



if __name__ == '__main__':
    start = time.time()
    fileurl = 'https://www.pinterest.com/v2_sitemaps/www_v2_board_sitemap.xml'
    print sys.argv
    main(fileurl, int(sys.argv[1]))
    print 'It took', time.time()-start, 'seconds.'