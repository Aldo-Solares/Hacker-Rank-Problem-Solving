
#LINK https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true

def minimumNumber(n, password):
    digit = False
    lower = False
    upper = False
    special = False
    security = [digit, lower, upper, special]
    lenght = 0
    for letter in range(len(password)):
        if password[letter].isdigit():
            lenght +=1
            security[0] = True
        elif password[letter].islower():
            lenght +=1
            security[1] = True
        elif password[letter].isupper():
            lenght +=1
            security[2] = True
        else:
            lenght +=1
            security[3] = True
    
    if lenght >= 6:
        return security.count(False)
    else: 
        missing = 6 - lenght
        if missing >= security.count(False):
            return missing
        else:
            return security.count(False)


if __name__ == '__main__':
    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)
