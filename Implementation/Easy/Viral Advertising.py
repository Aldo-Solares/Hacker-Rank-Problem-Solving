
#LINK https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true

import math

def viralAdvertising(n):
    shared = 5
    likes = 0
    for i in range(n):
        likes += math.floor(shared/2)
        shared = math.floor(shared/2)*3

    return likes

if __name__ == '__main__':
    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)
