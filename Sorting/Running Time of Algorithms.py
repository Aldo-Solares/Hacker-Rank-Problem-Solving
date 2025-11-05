
#LINK https://www.hackerrank.com/challenges/runningtime/problem?isFullScreen=true

def insertionSort2(n, arr):
    counter = 0
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            counter +=1
        arr[j + 1] = key

    print(counter)
                    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
