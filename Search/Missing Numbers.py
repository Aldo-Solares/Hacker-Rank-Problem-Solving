
#LINK https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true

from collections import Counter

def missingNumbers(arr, brr):
    dict_a = Counter(arr)
    dict_b = Counter(brr)
    
    missing = []
    
    for num in dict_b:
        if num not in dict_a:
            missing.append(num)
            
        elif dict_b[num] > dict_a[num]:
            missing.append(num)
            
    missing.sort()
    
    return missing

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(*result)