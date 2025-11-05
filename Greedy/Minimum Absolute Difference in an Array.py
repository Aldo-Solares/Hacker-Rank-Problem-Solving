
#LINK https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true

def minimumAbsoluteDifference(arr):
    n = len(arr)
    arr.sort()
    min_abs_diff = abs(arr[0]-arr[1])
    for i in range(n-1):
        abs_diff = abs(arr[i]-arr[i+1])
        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
    return min_abs_diff

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)