
#LINK https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true

def is_leap(year):
    if (year % 4) == 0 and (year % 100) != 0:  
        return True
    elif (year % 400) == 0 :
        return True
    else:
        return False
    return False


def dayOfProgrammer(year):
    leap = is_leap(year)
    if year > 1918:
        if leap:
            date = (f"{12}.09.{year}")
            return date  
        else:
            date = (f"{13}.09.{year}")
            return date
    elif year == 1918:
        date = (f"{26}.09.{year}")
        return date
    elif year <1918:
        if year%4==0:
            date = (f"{12}.09.{year}")
            return date
        else:
            date = (f"{13}.09.{year}")
            return date
        
if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)
