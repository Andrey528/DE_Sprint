import re

def brackets_validity():
    while True:
        brackets_dict = {')': '(', ']': '[', '}': '{'}
        keys_to_find = []

        input_string = input('Type string \n')

        clear_string = re.sub('[^\(\){}\[\]]', '', input_string)
        print(clear_string)

        for letter in clear_string:
            if letter in brackets_dict.values():
                for k, v in brackets_dict.items():
                    if v == letter:
                        keys_to_find.append(k)

            elif letter in keys_to_find:
                keys_to_find.remove(letter)

            else:
                print('False (Brackets dont match)')
                break

        if not keys_to_find: print('True (All brackets are closed)')
        else: print('False (Brackets dont match)')

        answer = input('Keep going brackets validity task? (y/n) \n')

        if answer == 'n':
            break

        elif answer != 'y':
            print('Incorrect input, keep going this task')