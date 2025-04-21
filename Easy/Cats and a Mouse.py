
#LINK https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true

def catAndMouse(x, y, z):
    a2m = abs(z-x)
    b2m = abs(z-y)
    if a2m < b2m:
        return "Cat A"
    elif a2m > b2m:
        return "Cat B"
    else:
        return "Mouse C"

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)