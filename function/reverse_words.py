def reverse_word(lst : list) -> list:
    lst2 = []
    for word in lst:
        lst2.append(word[::-1])
    return lst2 

lst = ['amir' , 'barbod' , 'negin']
print(reverse_word(lst))