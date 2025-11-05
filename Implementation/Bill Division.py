
#LINK https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true

def bonAppetit(bill, k, b):
    if (sum(bill)-bill[k])/2==b:
        print("Bon Appetit")
    else:
        print(int(b-(sum(bill)-bill[k])/2))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
