def palindrome():
    while True:
        word = input('Waiting input for palindrome task \n')
        if str(word.replace(' ', '')) == "".join(reversed(word.replace(' ', ''))):
            print('True (Palindrome)')
        else:
            print('False (Not Palindrome)')

        answer = input('Keep going palindrome task? (y/n) \n')
        if answer == 'n': break
        elif answer != 'y': print('Incorrect input, keep going this task')