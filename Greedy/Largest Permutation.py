
#LINK https://www.hackerrank.com/challenges/largest-permutation/problem?isFullScreen=true

def largestPermutation(k, arr):
    n = len(arr)
    pos = {v: i for i, v in enumerate(arr)}

    for i in range(n):
        max_val = n - i
        if arr[i] == max_val:
            continue
        max_val_index = pos[max_val]
        pos[arr[i]], pos[max_val] = max_val_index, i
        arr[i], arr[max_val_index] = arr[max_val_index], arr[i]
        k -= 1
        if k == 0:
            break
    return arr

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = largestPermutation(k, arr)
    print(*result)