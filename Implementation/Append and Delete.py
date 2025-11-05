
#LINK https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true

def appendAndDelete(s, t, k):
    common_length = 0
    min_len = min(len(s), len(t))
    for i in range(min_len):
        if s[i] == t[i]:
            common_length += 1
        else:
            break
    
    total_operations = (len(s) - common_length) + (len(t) - common_length)
    
    if k >= len(s) + len(t):
        return "Yes"
    elif total_operations <= k and (k - total_operations) % 2 == 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result)
