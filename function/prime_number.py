def prime(num : int) -> bool :
    c = 0
    for i in range(1,num+1):
        if num % i == 0:
            c +=1
    if c == 2:
        return True
    else:
        return False
    
num = int(input('Enter a number:'))
print(prime(num))