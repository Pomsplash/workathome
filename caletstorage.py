import sys
import os
import subprocess
from datetime import datetime

SAVE_DIR = "/tmp/test/storage"
SERVER_NAME = ['caletas1','caletas2']

def main():
    makeSavefolder()
    collectStorageData()

def makeSavefolder():
    path = SAVE_DIR + datetime.now().strftime("%Y%m%d")
    if os.path.isdir(path):
        print("File already exist ")
    else:
        cmd = "mkdir " + SAVE_DIR + datetime.now().strftime("%Y%m%d")
        print("Make file success")
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]

def collectStorageData():
    count = 0
    lenserver = len(SERVER_NAME)
    print(lenserver)

    while count < lenserver:
        print("test")
        nameoffile = SAVE_DIR + datetime.now().strftime("%Y%m%d") + '/' + SERVER_NAME[count]
        fopen = open(nameoffile,"w")
        cmd = "df -k --portability"
        ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
        print(ret)
        print >> fopen, datetime.now().strftime("%Y%m%d"),'\n\n',ret
        count+=1
    
        


if __name__ == "__main__":
    main()