
#LINK https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

from datetime import datetime

def timeConversion(s):

    military_time = datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")
    return military_time
    
if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
