
#LINK https://www.hackerrank.com/challenges/two-strings/problem?isFullScreen=true

def twoStrings(s1, s2):
    for x in s1:
        if x in s2:
            return "YES"
            
    return "NO"
    pass

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)
