
#LINK https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true

def closestNumbers(arr):
    arr.sort()
    n = len(arr)
    
    new_arr = []
    min_diff = abs(arr[0]-arr[1])
    
    for i in range(n-1):
        diff = abs(arr[i]-arr[i+1])
        
        if diff < min_diff:
            min_diff = diff
            new_arr = [arr[i], arr[i+1]]
            
        elif diff == min_diff:
            new_arr.append(arr[i])
            new_arr.append(arr[i+1])
            
    return new_arr

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(*result)
