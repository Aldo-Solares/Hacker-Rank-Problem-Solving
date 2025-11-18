
#LINK https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem?isFullScreen=true

def decentNumber(n):
    if n in [1, 2, 4, 7]:
        print(-1)
        return
    else:
        c_3 = 0
        c_5 = n
        while c_3%5 != 0 or c_5%3 != 0:
            c_5 -=5
            c_3 += 5
        
        number = "5"*c_5 + "3"*c_3
        
        print(number)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)