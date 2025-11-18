
#LINK https://www.hackerrank.com/challenges/a-chessboard-game-1/problem?isFullScreen=true

def chessboardGame(x, y):
    if ((x - 1) % 4 < 2) and ((y - 1) % 4 < 2):
        return "Second"
    return "First"

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])

        result = chessboardGame(x, y)

        print(result)
