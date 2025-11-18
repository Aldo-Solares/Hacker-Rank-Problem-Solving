

#LINK https://www.hackerrank.com/challenges/game-of-thrones/problem?isFullScreen=true

def gameOfThrones(s):
    odd_counter = 0
    my_set = set(s)
    for letter in my_set:
        if s.count(letter) % 2 == 1:
            odd_counter += 1
    
    if odd_counter == 0 or odd_counter == 1:
        return "YES"
    
    return "NO"

if __name__ == '__main__':
    s = input()
    
    result = gameOfThrones(s)

    print(result)