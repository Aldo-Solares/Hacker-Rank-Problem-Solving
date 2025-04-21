
#LINK https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true

from collections import Counter

def pickingNumbers(a):
    max_count = 0
    counter = Counter(a)
    for x in counter:
        current = counter[x] + counter.get(x+1, 0)
        max_count = max(max_count, current)
    
    return max_count

        
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)
