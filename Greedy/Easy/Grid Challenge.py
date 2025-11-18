
#LINK https://www.hackerrank.com/challenges/grid-challenge/problem?isFullScreen=true

def gridChallenge(grid):
    arr = []
    for line in grid:
        text = sorted(line)
        arr.append(text)
        
    n = len(arr[0])
    
    for i in range(n):
        for j in range(n-1):
            if ord(arr[j][i]) > ord(arr[j+1][i]):
                return "NO"
                
    return "YES"

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)