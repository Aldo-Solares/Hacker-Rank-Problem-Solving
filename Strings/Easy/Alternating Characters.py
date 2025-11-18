
#LINK https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true

def alternatingCharacters(s):
    counter = 0
    for x in range(len(s)-1):
        if s[x] == s[x+1]:
            counter +=1 
    return counter

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(result)