
#LINK https://www.hackerrank.com/challenges/halloween-sale/problem?isFullScreen=true

def howManyGames(p, d, m, s):
    games = 0
    while s > 0:
        s -=p
        p -=d
        if p < m:
            p = m
        if s >= 0:
            games +=1
        
    return games

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)
    
    print(answer)
