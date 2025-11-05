
#LINK https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true

def sockMerchant(n, ar):
    counter = 0
    mi_set = set(ar)
    for x in mi_set:
        counter += ar.count(x)//2
    
    return counter
    
if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
