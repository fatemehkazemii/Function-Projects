def number_type(lst : list) -> list:
    result = {}
    for i in lst:
        if i % 2 == 0:
             result[i] = 'even'
        else:
             result[i] = 'odd'
    return result
lst = []
for i in range(5):
    num = int(input('Enter a number:'))
    lst.append(num)
    
print(number_type(lst))