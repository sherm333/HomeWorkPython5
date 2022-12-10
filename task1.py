'''
Напишите программу, удаляющую из 
текста все слова содержащие "абв".
'''

check_text = 'Напишите абв программу, абв удаляющую изабв текста все слова содержащие "абв"'

def del_some_words(check_text):
    check_text = list(filter(lambda x: 'абв' not in x, check_text.split()))
    return " ".join(check_text)

check_text = del_some_words(check_text)
print(check_text)