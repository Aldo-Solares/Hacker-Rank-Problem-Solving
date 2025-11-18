
#LINK https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=true

def insertionSort1(n, arr):
    number = 0
    for x in range(-1,-len(arr),-1):
        if arr[x] < arr[x-1]:
            number = arr[x]
            arr[x] = arr[x-1]
            print(*arr)
            arr[x-1] = number
    print(*arr)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
