
#LINK https://www.hackerrank.com/challenges/lisa-workbook/problem?isFullScreen=true

def workbook(n, k, arr):
    page = 1
    special_problems = 0

    for problems in arr:
        for start in range(1, problems+1, k):
            end = min(start + k - 1, problems)
            if start <= page <= end:
                special_problems += 1
            page += 1
        
    return special_problems

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(result)