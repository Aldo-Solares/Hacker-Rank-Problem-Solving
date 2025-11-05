
#LINK https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true

import math
def squares(a, b):
    square_a = math.floor(math.sqrt(a))
    square_b = math.ceil(math.sqrt(b))
    result = [x*x for x in range(square_a,square_b+1) if x*x >= a and x*x <= b] 
    return len(result)

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        print(result)
    