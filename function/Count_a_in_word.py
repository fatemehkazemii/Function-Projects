#Count_a_in_word
def count_a(word:str)->int:
    c = 0
    for i in lword:
        if i == 'a' or i == 'A':
            c+=1
    return c  
lword = input('Enter a word:')
print(count_a(lword))