#Count_a_in_list
def count_a(lst:list)->list:
    lst2 = []
    for word in lst:
        c = 0
        for i in word:
            if i == 'a' or i == 'A':
                c+=1
        lst2.append(c)
    return lst2
lst = []
for i in range(4):
    word = input('Enter a word:')
    lst.append(word)
print(count_a(lst))