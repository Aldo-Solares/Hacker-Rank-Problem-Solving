
#LINK https://www.hackerrank.com/challenges/misere-nim-1/problem?isFullScreen=true

def misereNim(s):
    if all(x == 1 for x in s):
        return "First" if len(s) % 2 == 0 else "Second"

    x = 0
    for p in s:
        x ^= p
    return "First" if x != 0 else "Second"


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        print(result)
