
#LINK https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true

def minimumDistances(a):
    distance = 0
    min_distance = len(a)+1
    for x in range(len(a)):
        for y in range(distance,len(a)-1):
            y +=1
            if a[x] == a[y]:
                if min_distance > y-x:
                    min_distance = y-x
        distance +=1
        
    if min_distance == len(a)+1:
        return -1
    else:
        return min_distance
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(result)