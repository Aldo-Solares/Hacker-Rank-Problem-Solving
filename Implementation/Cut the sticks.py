
#LINK https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true

def cutTheSticks(arr):
    results = []
    arr = sorted(arr)
    while arr:
        results.append(len(arr))
        min_val = arr[0]
        arr = [x - min_val for x in arr if x - min_val > 0]
    return results

if __name__ == '__main__': 
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print("\n".join(map(str, result)))
