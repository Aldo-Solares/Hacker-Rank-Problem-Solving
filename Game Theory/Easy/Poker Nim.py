
#LINK https://www.hackerrank.com/challenges/poker-nim-1/problem?isFullScreen=true

def pokerNim(k, c):
    x = 0
    for pile in c:
        x ^= pile
    return "First" if x != 0 else "Second"

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        c = list(map(int, input().rstrip().split()))

        result = pokerNim(k, c)

        print(result)