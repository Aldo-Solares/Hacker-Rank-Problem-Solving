
#LINK https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true

def luckBalance(k, contests):
    contests = sorted(contests, key=lambda contests: (contests[1], contests[0]), reverse=True)
    luck = 0
    for l,t in contests:
        if k > 0 and t == 1:
            luck +=l
            k -=1
        elif k == 0 and t == 1:
            luck -=l
        else:
            luck +=l

    return luck

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(result)