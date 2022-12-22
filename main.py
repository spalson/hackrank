if __name__ == '__main__':
    number_of_numbers = int(input())

    numbers_list = set()

    for i in range(1, number_of_numbers + 1):
        numbers_list.add(i)

    print(numbers_list)
    #  dotad printuje liste po number_of_numbers
    number_of_commands = int(input())
    new_numbers = numbers_list

    for i in range(0, number_of_commands):
        user_cmd = input()
        if user_cmd.startswith("pop"):
            new_numbers.pop()
            print(new_numbers)
        if user_cmd.startswith("remove"):
            user_cmd_splitted = user_cmd.split()
            number_in_command = user_cmd_splitted[1]
            int_number_in_command = int(number_in_command)
            if int_number_in_command in new_numbers:
                new_numbers.remove(int_number_in_command)
                print(new_numbers)
            else:
                break
        if user_cmd.startswith("discard"):
            user_cmd_splitted = user_cmd.split()
            number_in_command = user_cmd_splitted[1]
            int_number_in_command = int(number_in_command)
            new_numbers.discard(int_number_in_command)
    print(new_numbers)
