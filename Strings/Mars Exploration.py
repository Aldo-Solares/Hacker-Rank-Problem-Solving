
#LINK https://www.hackerrank.com/challenges/mars-exploration/problem?isFullScreen=true

def marsExploration(s):
    message = "SOS"
    sos = [s[x:x+3] for x in range(0, len(s), 3)]
    difference = 0
    for messange in sos:
        for x in range(3):
            if messange[x] != message[x]:
                difference +=1
                
    return difference
    
if __name__ == '__main__':
    s = input()

    result = marsExploration(s)

    print(result)
