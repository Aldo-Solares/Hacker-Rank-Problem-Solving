
#LINK https://www.hackerrank.com/challenges/correctness-invariant/problem?isFullScreen=true

def insertion_sort(arr):
    while arr != sorted(arr):
        for x in range(len(arr)-1):
            if arr[x+1] < arr[x]:
                number = arr[x+1]
                for y in range(len(arr)):
                    if arr[y] > number:
                        arr.pop(x+1)
                        arr.insert(y,number)
                        break
        print(*arr)

m = int(input().strip())
arr = [int(i) for i in input().strip().split()]
insertion_sort(arr)