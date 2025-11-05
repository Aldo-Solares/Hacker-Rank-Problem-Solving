
#LINK https://www.hackerrank.com/challenges/separate-the-numbers/problem?isFullScreen=true

def separateNumbers(s):
    n = len(s)
    
    if n == 1:
        print("NO")
        return

    for length in range(1, n // 2 + 1):
        first_num = s[:length]
        if first_num[0] == '0':
            continue
        
        num = int(first_num)
        sequence = first_num
        
        while len(sequence) < n:
            num += 1
            sequence += str(num)
        
        if sequence == s:
            print(f"YES {first_num}")
            return
    
    print("NO")

    
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
