
#LINK https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=true

from collections import Counter

def happyLadybugs(b: str) -> str:
    n = len(b)
    counter = Counter(b)

    for color, c in counter.items():
        if color != '_' and c == 1:
            return "NO"

    if '_' in b:
        return "YES"
        
    for i in range(n):
        if not ((i > 0 and b[i] == b[i-1]) or(i < n-1 and b[i] == b[i+1])):
            return "NO"
            
    return "YES"
        
        

if __name__ == '__main__':
    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        print(result)
