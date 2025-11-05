
#LINK https://www.hackerrank.com/challenges/big-sorting/problem?isFullScreen=true

def bigSorting(unsorted):
    unsorted.sort(key=lambda x: (len(x), x))
    return unsorted

if __name__ == '__main__':
    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    print("\n".join(map(str, result)))
