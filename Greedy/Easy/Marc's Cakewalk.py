
#LINK https://www.hackerrank.com/challenges/marcs-cakewalk/problem?isFullScreen=true

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    miles = 0
    for j, cupcake in enumerate(calorie):
        miles += 2**j*cupcake
    return miles

if __name__ == '__main__':
    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(result)
