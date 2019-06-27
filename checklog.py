import os 
import sys
from datetime import datetime

def main():
    print("test")
    dateconvert()

def dateconvert():
    print(startdate)
    print(enddate)
    startdate_convert = datetime.strptime(startdate,'%Y%m%d')
    enddate_convert = datetime.strptime(enddate,'%Y%m%d')
    print(startdate_convert)
    print(enddate_convert)

if __name__ == "__main__":
    startdate = sys.argv[1]
    enddate = sys.argv[2]
    main()