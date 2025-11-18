
#LINK https://www.hackerrank.com/challenges/the-love-letter-mystery/problem?isFullScreen=true

def theLoveLetterMystery(s):
    counter = 0
    n = int(len(s)/2)
    left = 0
    right = len(s)-1
    
    for x in range(n):
        counter += abs(ord(s[left]) - ord(s[right]))
        left += 1
        right -= 1
        
    return counter

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(result)
