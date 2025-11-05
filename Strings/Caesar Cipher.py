
#LINK https://www.hackerrank.com/challenges/caesar-cipher-1/problem?isFullScreen=true

def caesarCipher(s, k):
    encrypted = ""

    for letra in s:
        if letra.isalpha():
            base = 'A' if letra.isupper() else 'a'
            new_position = (ord(letra) - ord(base) + k) % 26
            encrypted += chr(ord(base) + new_position)
        else:
            encrypted += letra

    return encrypted

if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)
