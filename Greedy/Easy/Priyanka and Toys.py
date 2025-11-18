
#LINK https://www.hackerrank.com/challenges/priyanka-and-toys/problem?isFullScreen=true

def toys(w):
    n = len(w)
    w.sort()
    containers = 1
    min_w = w[0]+4
    
    for i in range(1, n):
        if w[i]>min_w:
            containers +=1
            min_w = w[i]+4

    return containers
    
if __name__ == '__main__':
    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    print(result)