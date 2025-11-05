
#LINK https://www.hackerrank.com/challenges/weighted-uniform-string/problem?isFullScreen=true

def weightedUniformStrings(s, queries):
    weights = set()
    prev = ''
    curr_weight = 0

    for c in s:
        w = ord(c) - 96
        if c == prev:
            curr_weight += w
        else:
            curr_weight = w
            prev = c
        weights.add(curr_weight)

    return ["Yes" if q in weights else "No" for q in queries]

if __name__ == '__main__':
    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    print("\n".join(result))
