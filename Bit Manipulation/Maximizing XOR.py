
#LINK https://www.hackerrank.com/challenges/maximizing-xor/problem?isFullScreen=true

def maximizingXor(l, r):
    max_value = 0
    for x in range(l,r+1):
        for y in range(x, r+1):
            value = x^y
            if value > max_value:
                max_value = value
    
    return max_value
    
if __name__ == '__main__':
    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    print(result)
    
#Nota - Mejor metodo

def maximizingXor(l, r):
    return (1 << (r ^ l).bit_length()) - 1
