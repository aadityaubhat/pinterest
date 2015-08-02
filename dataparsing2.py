__author__ = 'aaditya'

import time,os
for line in file("www_v2_board_sitemap.xml"):
	if '</loc>' in line:
		os.system("cd data;wget {}".format(line.strip().replace('<loc>','').replace('</loc>','')))
