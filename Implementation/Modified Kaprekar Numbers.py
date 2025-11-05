
#LINK https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true

def kaprekarNumbers(p, q):
    number_list = range(p,q+1)
    kaprekar_numbers = []
    
    for num in number_list:
        square_number = str(num*num)
        
        if len(square_number) == 1:
            total = int(square_number)
            
        else:
            total = int(square_number[:int(len(square_number)/2)]) + int(square_number[int(len(square_number)/2):])
            
        if total == num:
            kaprekar_numbers.append(num)
    if kaprekar_numbers:
        print(*kaprekar_numbers)
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
