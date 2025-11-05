
#LINK https://www.hackerrank.com/challenges/cavity-map/problem?isFullScreen=true

def cavityMap(grid):
    for maps in range(1,len(grid)-1):
        new_cell = grid[maps][0]
        for cells in range(1,len(grid)-1):
            current = grid[maps][cells]
            up = grid[maps-1][cells]
            left = grid[maps][cells-1]
            down = grid[maps+1][cells]
            right = grid[maps][cells+1]
            if current > up and current > left and current > down and current > right:
                new_cell += "X"
            else:
                new_cell +=current
        new_cell += grid[maps][-1]
        grid[maps] = new_cell
    return grid

if __name__ == '__main__':
    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print("\n".join(result))