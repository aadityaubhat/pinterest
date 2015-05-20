__author__ = 'aaditya'

import xml.etree.ElementTree
import urllib
import gzip
import os

def parse_link(link):
    #download xml file;
    #check if the file exists or else download;
    if not (os.path.isfile('data_aaditya/mainlink.xml')):
        file = urllib.URLopener()
        file.retrieve(link, "data_aaditya/mainlink.xml")
    root = xml.etree.ElementTree.parse("data_aaditya/mainlink.xml").getroot()
    result = {}
    for i in xrange(0,len(root)):
        result[i] = root[i][0].text, root[i][1].text.rsplit('T')[0]
    return result

def parse_gz(lst):
    if not (os.path.isfile(('b:/pinterest/data_aaditya/'+lst[0].rsplit('/')[4]))):
        file = urllib.URLopener()
        file.retrieve(lst[0], ('b:/pinterest/data_aaditya/'+lst[0].rsplit('/')[4]))
    f = gzip.open(('b:/pinterest/data_aaditya/'+lst[0].rsplit('/')[4]), 'rb')
    root = xml.etree.ElementTree.fromstring(f.read())
    f.close()
    result = {}
    for i in xrange(0,len(root)):
        result[i] = root[i][0].text, lst[1]
    return result

def slicelink(lst):
    return lst[0].rsplit('/')[3], lst[0].rsplit('/')[4], lst[1]

def main(fileurl,n=100):
    linklist = parse_link(fileurl)
    gzfiles = {}
    data = []
    for i in xrange(0,n):
        gzfiles[i] = parse_gz(linklist[i])
        for j in xrange(0, len(gzfiles[i])):
            data.append(slicelink(gzfiles[i][j]))
    return data

if __name__ == '__main__':
    fileurl = 'https://www.pinterest.com/v2_sitemaps/www_v2_board_sitemap.xml'
    main(fileurl,500)