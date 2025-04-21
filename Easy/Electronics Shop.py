
#LINK https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true

from itertools import product

def getMoneySpent(keyboards, drives, b):
    combinations = product(keyboards,drives)
    money = -1
    for x in combinations:
        if sum(x) > money and sum(x) <= b:
            money = sum(x)
    return money

if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)
