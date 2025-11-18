
#LINK https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true

def icecreamParlor(m, arr):
    money_spent={}
    i = 1
    for num in arr:
        target = m-num
        if target in money_spent:
            return money_spent[target],i
        money_spent[num] = i
        i += 1
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        print(*result)

