
#LINK https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true

def findDigits(n):
    counter = 0
    numbers_list = list(map(int, str(n)))
    for number in numbers_list:
        if number != 0 and n%number == 0:
            counter += 1
    return counter

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        print(result)
