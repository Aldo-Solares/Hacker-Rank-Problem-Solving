
#LINK https://www.hackerrank.com/challenges/quicksort1/problem?isFullScreen=true

def quickSort(arr):
    pivot = arr[0]
    left = []
    equal = []
    right = []
     
    for x in arr:
        if x<pivot:
            left.append(x)
        elif x==pivot:
            equal.append(x)
        else:
            right.append(x)

    return left+equal+right
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    print(*result)
