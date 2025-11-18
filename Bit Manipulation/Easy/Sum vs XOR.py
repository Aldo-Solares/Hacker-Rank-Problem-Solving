
#LINK https://www.hackerrank.com/challenges/sum-vs-xor/problem?isFullScreen=true

def sumXor(n):
    if n == 0:
        return 1
        
    count_zero_bits = 0
    while n > 0:
        if (n & 1) == 0:
            count_zero_bits += 1
        n >>= 1
    
    return 1 << count_zero_bits

if __name__ == '__main__':
    n = int(input().strip())

    result = sumXor(n)

    print(result)
