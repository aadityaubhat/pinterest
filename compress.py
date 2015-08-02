__author__ = 'aaditya'

import gzip,glob,logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='compress.log',
                    filemode='w')
output = gzip.open("data.gz",'w')
for fname in glob.glob("data/*.gz"):
	try:
		f = gzip.open(fname)
		for line in f:
			if line.startswith("<loc>"):
				entries = line.split('/')
				output.write("\t".join([entries[-4],entries[-3].replace("<","")])+"\n")
		f.close()
	except:
		logging.info(fname)
		pass
output.close()
