
#LINK https://www.hackerrank.com/challenges/lonely-integer/problem?isFullScreen=true

from collections import Counter

def lonelyinteger(a):
    frec = dict(Counter(a))
    for x in frec:
        if frec.get(x) == 1:
            return x 
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)
    
#Nota - Mejor metodo

def lonelyinteger(a):
    res = 0
    for x in a:
        res ^= x
    return res

