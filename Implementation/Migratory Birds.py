
#LINK https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true

import collections

def migratoryBirds(arr):

    results = collections.Counter(arr)
    most_common = list(results.most_common())
    most_common = sorted(most_common, key=lambda x: (-x[1], x[0]))
    return most_common[0][0]

if __name__ == '__main__':
    #arr_count = int(input().strip())
    arr_count = 11
    
    #arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
    result = migratoryBirds(arr)
    
    print(result)