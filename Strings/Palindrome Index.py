
#LINK https://www.hackerrank.com/challenges/palindrome-index/problem?isFullScreen=true

def palindromeIndex(s):
    start = 0
    end = len(s)-1 
    while start < end:
        if s[start] != s[end]:
            if s[:start]+s[start+1:] == (s[:start]+s[start+1:])[::-1]:
                return start
            else:
                return end
        start +=1
        end -=1  
    return -1
    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(result)
