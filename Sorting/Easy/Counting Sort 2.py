
#LINK https://www.hackerrank.com/domains/algorithms?filters%5Bstatus%5D%5B%5D=unsolved&filters%5Bdifficulty%5D%5B%5D=easy&filters%5Bsubdomains%5D%5B%5D=arrays-and-sorting&badge_type=problem-solving

def countingSort(arr):
    zeros = [0] * 100
    
    for x in arr:
        zeros[x] += 1

    result = []
    for i, c in enumerate(zeros):
        result.extend([i] * c)
    
    return result

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().split()))
    result = countingSort(arr)
    print(*result)