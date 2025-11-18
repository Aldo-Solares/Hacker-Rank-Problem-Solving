
#LINK https://www.hackerrank.com/challenges/beautiful-pairs/problem?isFullScreen=true

def beautifulPairs(A, B):
    from collections import Counter

    n = len(A)
    freqA = Counter(A)
    freqB = Counter(B)

    base = 0
    for x in freqA:
        base += min(freqA[x], freqB.get(x, 0))
        
    if base < n:
        return base + 1
    else:
        return base - 1

if __name__ == '__main__':
    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    print(result)