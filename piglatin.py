repeat = True
while repeat:
    pig = 'ay'
    original = input('Enter a word: ')
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = word + first + pig
        new_word = new_word[1:len(new_word)].title()
        print(new_word)
    else:
        print('empty')
    again = input('Again? y/n ')
    if again == 'y':
        repeat = True
    elif again == 'n':
        repeat = False
        