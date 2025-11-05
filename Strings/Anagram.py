
#LINK https://www.hackerrank.com/challenges/anagram/problem?isFullScreen=true

def anagram(s):
    n = int(len(s)/2)
    counter = 0
    if len(s) % 2 == 1:
        return -1
    else:
        a = list(s[0:n])
        b = list(s[n:len(s)])
        for x in a:
            if x in b:
                b.remove(x)
            else:
                counter +=1
    return counter
            

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(result)
