
#LINK https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true

def hurdleRace(k, height):
    result = max(height)-k
    if result < 0:
        return 0
    return result

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(result)