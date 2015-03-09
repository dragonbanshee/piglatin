repeat = True
while repeat:
    pig = 'ay'
    vpig = 'way'
    original = input('Enter a word: ')
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
            new_word = word + vpig
            new_word = new_word.title()
        else:
            new_word = word + first + pig
            new_word = new_word[1:len(new_word)].title()
        print(new_word)
    else:
        print('You did not enter a valid string.')
    again = input('Again? y/n ')
    if again == 'y':
        repeat = True
    elif again == 'n':
        repeat = False
        