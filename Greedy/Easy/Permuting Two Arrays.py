
#LINK https://www.hackerrank.com/challenges/two-arrays/problem?isFullScreen=true

def twoArrays(k, A, B):
    n = len(A)
    
    A.sort()
    B.sort(reverse=True)
    
    for i in range(n-1):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"
    
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        print(result)
