
#LINK https://www.hackerrank.com/challenges/making-anagrams/problem?isFullScreen=true

def makingAnagrams(s1, s2):
    a = list(s1)
    b = list(s2)
    for x in s1:
        if x in b:
            a.remove(x)
            b.remove(x)
    
    return len(a) + len(b)

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    print(result)