#Starts-with_a

def starts_with_a(lst):
    lst2 = []
    for i in lst:
        if i[0] == 'a' or i =='A':
            lst2.append(i)

    return lst2       
lst = ['ayda','amir','reza','ahmad'] 
print(starts_with_a(lst))