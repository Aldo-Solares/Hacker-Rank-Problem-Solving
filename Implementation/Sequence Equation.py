
#LINK https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true

def permutationEquation(p):
    value_index = {val: i+1 for i, val in enumerate(p)}
    result = []
    for x in range(1, len(p)+1):
        y = value_index[x]
        z = value_index[y]
        result.append(z)
    
    return result
    
if __name__ == '__main__':
    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print("\n".join(map(str, result)))