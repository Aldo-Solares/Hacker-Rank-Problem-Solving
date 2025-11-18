
#LINK https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true

def maximumToys(prices, k):
    prices.sort()
    money = 0
    count = 0
    for price in prices:
        if money + price > k:
            break
        money += price
        count += 1
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    
    print(result)
