
#LINK https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem?isFullScreen=true

def maximumPerimeterTriangle(sticks):
    n = len(sticks)
    sticks.sort(reverse=True)
    
    for i in range(n-2):
        if sticks[i+2] + sticks[i+1] > sticks[i]:
            return [sticks[i+2],sticks[i+1],sticks[i]]
        
    return [-1]
    
if __name__ == '__main__':
    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    print(*result)
