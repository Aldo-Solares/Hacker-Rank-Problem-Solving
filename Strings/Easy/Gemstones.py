
#LINK https://www.hackerrank.com/challenges/gem-stones/problem?isFullScreen=true

def gemstones(arr):
    my_Set = set(arr[0])
    for mineral in arr:
        my_Set = my_Set.intersection(set(mineral))
            
    if my_Set:
        return len(my_Set)
        
    return 0

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    print(result)
