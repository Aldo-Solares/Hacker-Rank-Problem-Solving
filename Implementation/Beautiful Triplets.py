
#LINK https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true

def beautifulTriplets(d, arr):
    my_set = set(arr)
    count = 0
    for a in arr:
        if (a + d) in my_set and (a + 2*d) in my_set:
            count += 1
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(result)
