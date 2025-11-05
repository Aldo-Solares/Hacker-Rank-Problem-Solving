
#LINK https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true

def countingValleys(steps, path):
    valleys_counter = 0
    current_level = 0
    for x in range(len(path)):
        if path[x] == "U" and current_level == -1:
            valleys_counter +=1
            current_level +=1
        elif path[x] == "U":
            current_level +=1
        elif path[x] == "D":
            current_level -=1
    return valleys_counter

if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)