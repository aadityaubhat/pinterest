__author__ = 'aaditya'
import pymongo
from config import USERNAME
from config import PASSWORD
from config import HOST
from config import PORT
from config import DBNAME

DB = pymongo.MongoClient('mongodb://'+USERNAME+':'+PASSWORD+'@'+HOST+':'+PORT+'/'+DBNAME)
