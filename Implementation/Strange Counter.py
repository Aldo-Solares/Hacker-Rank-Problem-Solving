
#LINK https://www.hackerrank.com/challenges/strange-code/problem?isFullScreen=true
def strangeCounter(t):
    cicle = 3
    value = 3
    while t > value:
        cicle = cicle * 2
        value += cicle
    
    return value - t + 1
    

if __name__ == '__main__':
    t = int(input().strip())

    result = strangeCounter(t)

    print(result)
