def arabic_number_to_roman():
    while True:
        while True:
            arabic_number = input('Which arabic number you want convert to roman? \n')
            if int(arabic_number) < 1 or int(arabic_number) > 2000:
                print('Incorrect number')
            else: break

        rom_number = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        str_arabic = str(arabic_number)
        arabic_reverse = str_arabic[::-1]
        arabic_length = len(arabic_reverse)
        rom_result = ""
        rom_pointer = 0

        for place in range(arabic_length):
            if arabic_reverse[place] in ["0", "1", "2", "3"]:
                rom_result = rom_number[rom_pointer] * int(arabic_reverse[place]) + rom_result
            elif arabic_reverse[place] in ["4"]:
                rom_result = rom_number[rom_pointer] + rom_number[rom_pointer + 1] + rom_result
            elif arabic_reverse[place] in ["5", "6", "7", "8"]:
                rom_result = rom_number[rom_pointer + 1] + rom_number[rom_pointer] * (int(arabic_reverse[place]) - 5) + rom_result
            elif arabic_reverse[place] in ["9"]:
                rom_result = rom_number[rom_pointer] + rom_number[rom_pointer + 2] + rom_result
            rom_pointer += 2

        print('Roman number will be ' + rom_result)

        answer = input('Keep going arabic to roman task? (y/n) \n')
        if answer == 'n': break
        elif answer != 'y': print("Incorrect input, keep going this task")
