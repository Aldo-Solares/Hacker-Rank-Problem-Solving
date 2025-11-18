
#LINK https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true

def jumpingOnClouds(c):
    position = 0
    jumps = 0
    while position < len(c)-1:
        if position+2 < len(c) and c[position+2] == 0:
            position +=2
        elif c[position+1] == 0:
            position +=1
        jumps +=1
    return jumps
        
if __name__ == '__main__':
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)
