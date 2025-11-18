
#LINK https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true

import re
def superReducedString(s):
    while s:
        if s == re.sub(r"(\D)\1{1}","",s):
            break
        else:
            s = re.sub(r"(\D)\1{1}","",s)
    return s
        
if __name__ == '__main__':
    s = input()

    result = superReducedString(s)
    
    if result:
        print("".join(result))
    else:
        print("Empty String")
