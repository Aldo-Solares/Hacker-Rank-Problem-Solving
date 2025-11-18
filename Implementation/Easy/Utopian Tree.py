
#LINK https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true

def utopianTree(n):
    height = 1
    for x in range(n+1):
        if x % 2 == 0 and x != 0:
            height +=1
        elif x % 2 != 0 and x != 0:
            height = 2*height
    return height

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        print(result)