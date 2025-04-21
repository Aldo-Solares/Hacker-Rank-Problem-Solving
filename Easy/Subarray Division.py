
#LINK https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true

def birthday(s, d, m):
    square_counter = 0
    steps = len(s)-m+1
    for x in range(steps):
        if sum(s[x:m+x]) == d:
            square_counter +=1
        
    return square_counter
if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(result)