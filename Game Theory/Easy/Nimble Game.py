
#LINK https://www.hackerrank.com/challenges/nimble-game-1/problem?isFullScreen=true

def nimbleGame(s):
    x = 0
    for i, coins in enumerate(s):
        if coins % 2 == 1:
            x ^=i
    return "First" if x != 0 else "Second"

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = nimbleGame(s)

        print(result)