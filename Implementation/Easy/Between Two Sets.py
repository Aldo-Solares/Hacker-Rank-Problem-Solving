
#LINK https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true

import math

def getTotalX(a, b):
    min_mult_a = math.lcm(*a)
    max_mult_b = math.gcd(*b)
    
    contador_1 = min_mult_a
    
    set_lcm = set()
    
    while contador_1 <= max_mult_b:
        set_lcm.add(contador_1)
        contador_1 += min_mult_a

    set_gcd = set([i for i in range(1, max_mult_b + 1) if max_mult_b % i == 0])
    
    len_result = len(set_lcm.intersection(set_gcd))
    
    return len_result
    
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
    
    print(total)