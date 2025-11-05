
#LINK https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?isFullScreen=true

def hackerrankInString(s):
    target = "hackerrank"
    index = 0
    for letter in range(len(s)):
        if s[letter] == target[index]:
            index +=1
        if index >= 10:
            return "YES"
    return "NO"

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result)
