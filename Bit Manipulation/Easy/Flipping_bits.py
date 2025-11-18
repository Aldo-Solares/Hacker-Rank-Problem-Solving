
#LINK https://www.hackerrank.com/challenges/flipping-bits/problem?isFullScreen=true

def flippingBits(n):
    a = (bin(n)[2:])
    b = ""
    for i in a:
        if i == "0":
            b +="1"
        else:
            b +="0"
            
    n_one = 32-len(a)
    a = n_one*"1"+b
    return int(a,2)

#Nota - Mejor metodo

def flippingBits(n):
    MASK_32BIT = 0xFFFFFFFF
    return n ^ MASK_32BIT