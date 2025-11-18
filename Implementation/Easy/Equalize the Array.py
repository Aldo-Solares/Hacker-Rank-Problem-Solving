 
#LINK https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true

def equalizeArray(arr):
    max_counter = 0
    for x in arr:
        if max_counter < arr.count(x):
            max_counter = arr.count(x)
    return len(arr) - max_counter

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)