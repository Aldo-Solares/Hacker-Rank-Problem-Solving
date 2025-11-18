
#LINK https://www.hackerrank.com/challenges/find-the-median/problem?isFullScreen=true

def findMedian(arr):
    arr.sort()
    n = len(arr)
    
    return arr[n//2]
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    print(result)
