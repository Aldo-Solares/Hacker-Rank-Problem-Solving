
#LINK https://www.hackerrank.com/challenges/countingsort1/problem?isFullScreen=true

def countingSort(arr):
    zeros = [0]*100
    
    for x in arr:
        zeros[x] +=1
    
    return zeros

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(*result)