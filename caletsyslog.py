import os 
import sys
from datetime import datetime,time,timedelta
import glob
import re
import subprocess

LOG_DIR = '/var/log/syslog/*/*/*/*.log'
SAVE_DIR = '/tmp/test/syslog_'
SERVER_NAME = ['caletas1','caletas2','caletas3','caletas4','caletql2']

def main():
    date_list = dateConvert()
    file_list = getFilelog()
    makefolder()
    collectlog(date_list,file_list)
    
def dateConvert():
    date_list = []
    startdate_convert = datetime.strptime(startdate,'%Y%m%d')
    enddate_convert = datetime.strptime(enddate,'%Y%m%d')
    diffdate =  enddate_convert - startdate_convert
    
    for i in range(diffdate.days +1):
        x = startdate_convert+timedelta(days=i)
        y = x.strftime("%Y%m%d")
        date_list.append(y)     
    return date_list

def getFilelog():
    file_list = []
    dir = glob.glob(LOG_DIR)
    for d in dir:
        file_list.append(d)
    return file_list

def makefolder():
    path = SAVE_DIR  + datetime.now().strftime('%Y%m%d')
    if os.path.isdir(path):
        print("File already exist")
    else:
        cmd = "mkdir " + SAVE_DIR  + datetime.now().strftime('%Y%m%d')
        print("Make file success")
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]

def collectlog(date_list,file_list):
    count = 0
    lenserver = len(SERVER_NAME)
  
    while count < lenserver:
        i=0
        nameoffile = SAVE_DIR + datetime.now().strftime('%Y%m%d') + '/' +SERVER_NAME[count] + '.txt'
        fopen = open(nameoffile, "w")
        
        r = re.compile(r'w*(%s)\w*'%SERVER_NAME[count])
        select = filter(r.search,file_list)
        lengthdatelist = len(date_list)
        
        while i < lengthdatelist:
            if any(date_list[i] in s for s in select):
                rex = re.compile(r'\S+\w*(%s)\w*.\w*'%date_list[i])
                filenamelist = filter(rex.match,select)
                filename = ''.join(filenamelist)
                fread = open(filename,"r")
                lines = fread.read()
                print >>fopen, date_list[i],'\n',lines
            else:
                print >>fopen, date_list[i],'\n',"None",'\n'

            i+=1

        fopen.close()    
        count+=1

if __name__ == "__main__":
    startdate = sys.argv[1]
    enddate = sys.argv[2]
    main()