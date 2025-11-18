
#LINK https://www.hackerrank.com/challenges/sherlock-and-array/problem?isFullScreen=true

def balancedSums(arr):
    arr_sum = sum(arr)
    left_sum = 0
    for i in arr:
        if left_sum == arr_sum-left_sum-i:
            return "YES"
        left_sum += i
    return "NO"

if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result)
