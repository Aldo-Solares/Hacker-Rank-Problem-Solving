
#LINK https://www.hackerrank.com/challenges/service-lane/problem?isFullScreen=true

def serviceLane(n, cases, width):
    result_list = [min(width[x:y+1]) for x,y in cases]
    return result_list 

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases, width)
    
    print("\n".join(map(str, result)))