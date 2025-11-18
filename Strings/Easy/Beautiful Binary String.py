
#LINK https://www.hackerrank.com/challenges/beautiful-binary-string/problem?isFullScreen=true

def beautifulBinaryString(b):
    moves = 0
    i = 0
    right = len(b)-3
    while "010" in b and i<= right:
        if b[i] == "0" and b[i+1] == "1" and b[i+2] == "0":
            b = b[:i+2]+"1"+b[i+3:]
            moves += 1
        i+=1
    
    return moves
    
if __name__ == '__main__':
    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    print(result)
