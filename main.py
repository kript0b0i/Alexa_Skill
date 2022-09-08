import sys, getopt
import scraper
from selenium.common.exceptions import NoSuchElementException

address = ''
store = ''
try:
    opts, args = getopt.getopt(sys.argv[1:],"a:s:",["address","store"])
except getopt.GetoptError:
    print ('[USAGE]: main.py -a <"address"> -s <store>')
    sys.exit(2)
if(len(sys.argv) ==5):
    for opt, arg in opts:
        if opt  == '-a':
            address = arg 
        if opt == '-s':
            store = arg      
    if(address == '' and store == ''):
        print("Please check your arguments")
        sys.exit()
    else:
         scraper.ScraperLogic(address, store) 
            
          
else:
    print('[USAGE]: main.py -a <"address"> -s <store>')
    