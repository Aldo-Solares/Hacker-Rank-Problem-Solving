
#LINK https://www.hackerrank.com/challenges/funny-string/problem?isFullScreen=true

def funnyString(s):
    n = len(s)-1
    string = [abs(ord(s[x])-ord(s[x+1])) for x in range(n)]
    rs = s[::-1]
    reverstring = [abs(ord(rs[x])-ord(rs[x+1])) for x in range(n)]
    
    for y in range(n):
        if string[y] != reverstring[y]:
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        print(result)
