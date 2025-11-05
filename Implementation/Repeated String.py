
#LINK https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true

def repeatedString(s, n):
    count_a = s.count("a")
    len_s = len(s)
    if not (n/len_s).is_integer():
        return (n//len_s)*count_a + s[0:n%len_s].count("a")
        
    return (n//len_s)*count_a

if __name__ == '__main__':
    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)