
#LINK https://www.hackerrank.com/challenges/flatland-space-stations/problem?isFullScreen=true

def flatlandSpaceStations(n, c):
    c.sort()
    max_dist = 0

    max_dist = max(max_dist, c[0])

    for i in range(1, len(c)):
        dist = (c[i] - c[i-1]) // 2
        max_dist = max(max_dist, dist)

    max_dist = max(max_dist, n - 1 - c[-1])

    return max_dist


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(result)
