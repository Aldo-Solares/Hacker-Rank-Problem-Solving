
#LINK https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true

def angryProfessor(k, a):
    counter = 0
    for x in a:
        if x <= 0:
            counter += 1
        if counter >= k:
            return "NO"
    return "YES"
            
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n, k = map(int, input().split())

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result)
