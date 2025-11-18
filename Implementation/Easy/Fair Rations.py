
#LINK https://www.hackerrank.com/challenges/fair-rations/problem?isFullScreen=true

def fairRations(B):
    odds = len([x for x in B if x%2==1])
    breads = 0
    
    while odds != 0:
        if odds == 1:
            return "NO"
            
        for x in range(len(B)-1):
            if B[x] % 2 == 1:
                B[x] +=1
                B[x+1] +=1
                breads +=2 
        odds = len([x for x in B if x%2==1])

    return breads
        
        

if __name__ == '__main__':
    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    print(result)