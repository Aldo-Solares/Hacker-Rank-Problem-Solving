
#LINK https://www.hackerrank.com/challenges/pangrams/problem?isFullScreen=true

import string

def pangrams(s):
    alphabet = list(string.ascii_lowercase)
    
    for letter in s:
        if letter.lower() in alphabet:
            alphabet.pop(alphabet.index(letter.lower()))

    if alphabet:
        return "not pangram"
        
    return "pangram"
    
if __name__ == '__main__':
    s = input()

    result = pangrams(s)

    print(result)
