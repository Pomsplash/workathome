import os 
import sys
from datetime import datetime,time,timedelta
import glob
import re

DIR_NAME = '/var/log/syslog/*/*/*/*.log'
SAVE_FILE = '/tmp/test'

def main():
    date_list = dateconvert()
    filelog = filelist()
    collectlog(date_list,filelog)

def dateconvert():
    date_list = []
    startdate_convert = datetime.strptime(startdate,'%Y%m%d')
    enddate_convert = datetime.strptime(enddate,'%Y%m%d')
    diffdate =  enddate_convert - startdate_convert
    
    for i in range(diffdate.days +1):
        x = startdate_convert+timedelta(days=i)
        y = x.strftime("%Y%m%d")
        date_list.append(y)     
        
    print(date_list)
    return date_list

def filelist():
    filelog = []
    dir = glob.glob(DIR_NAME)
    for d in dir:
        filelog.append(d)

    #print(filelog)
    return filelog

def collectlog(date_list,filelog):
    r = re.compile(r'w*\caletas1\w*')
    select = filter(r.search,filelog)
    print(select)
    
    #for i in date_list:
       # if re.match()
        
        

    
if __name__ == "__main__":
    startdate = sys.argv[1]
    enddate = sys.argv[2]
    main()