
#LINK https://www.hackerrank.com/challenges/manasa-and-stones/problem?isFullScreen=true

def stones(n, a, b):
    resultados = set()
    for k in range(n):
        resultados.add(k * a + (n - 1 - k) * b)
    return sorted(resultados)

if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        print(*result)