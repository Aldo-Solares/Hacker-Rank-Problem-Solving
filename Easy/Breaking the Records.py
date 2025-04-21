
#LINK https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    count_max = 0
    count_min = 0
    for x in scores:
        if x > max_score:
            count_max += 1
            max_score = x
        elif x < min_score:
            count_min += 1
            min_score = x
    list_results=[count_max,count_min]
    return list_results

if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    
    print(*result)