
#LINK https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr) - arr[-1]
    max_sum = sum(arr) - arr[0]
    print(f"{min_sum} {max_sum}")
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
