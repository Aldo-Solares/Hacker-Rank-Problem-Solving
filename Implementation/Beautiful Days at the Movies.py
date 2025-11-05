
#LINK https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true

def beautifulDays(i, j, k):
    list_days_str = list(map(str, [x for x in range(i,j+1)]))
    list_days_int = list(range(i,j+1))
    reverse_list_days = list([int(x[::-1]) for x in list_days_str])
    perfect_days = 0
    for x in range(len(list_days_int)):
        if (list_days_int[x]-reverse_list_days[x])%k == 0:
            perfect_days +=1
        
    return perfect_days

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    print(result)