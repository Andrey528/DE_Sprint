def convert_to_dec(binary_number):
    dec_number = 0

    for i in range(0, len(binary_number)):
        dec_number = dec_number + int(binary_number[i]) * (2 ** (len(binary_number) - i - 1))

    return dec_number

def convert_to_bin(dec_number):
    binary_number = '';

    while dec_number > 0:
        binary_number = str(dec_number % 2) + binary_number
        dec_number = dec_number // 2

    return binary_number

def multiplay_binary():
    while True:
        first_number = input('Enter first number \n')
        second_number = input('Enter second number \n')

        first_dec_number = convert_to_dec(first_number)
        second_dec_number = convert_to_dec(second_number)

        print('The result is ' + convert_to_bin(first_dec_number * second_dec_number))

        answer = input('Keep going multiply task? (y/n) \n')
        if answer == 'n': break
        elif answer != 'y': print('Incorrect input, keep going this task')