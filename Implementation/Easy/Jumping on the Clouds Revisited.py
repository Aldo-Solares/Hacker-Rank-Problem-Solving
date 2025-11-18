
#LINK http://hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true

def jumpingOnClouds(c, k):
    energy = 100
    counter = 0
    while True:
        counter +=k
        if counter >= len(c):
            counter -=len(c)
            
        if c[counter] == 1:
            energy -=1+2
        else:
            energy -=1
            
        if counter == 0:
            break
    return energy
    
    
if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)