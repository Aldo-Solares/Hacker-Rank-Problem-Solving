
#LINK https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true

from itertools import combinations

def divisibleSumPairs(n, k, ar):
    list_combinations = list(combinations(ar,2))
    counter=0
    for x in list_combinations:
        if sum(x)%k == 0:
            counter +=1
    return counter

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
