
#LINK https://www.hackerrank.com/challenges/camelcase/problem?isFullScreen=true

def camelcase(s):
    counter = 1
    for x in range(len(s)):
        if s[x].isupper():
            counter +=1
            
    return counter

if __name__ == '__main__':
    s = input()

    result = camelcase(s)

    print(result)
