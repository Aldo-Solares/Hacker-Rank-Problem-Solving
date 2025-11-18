
#LINK https://www.hackerrank.com/challenges/game-of-stones-1/problem?isFullScreen=true

def gameOfStones(n):
    return "Second" if n % 7 in (0, 1) else "First"
        
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        print(result)