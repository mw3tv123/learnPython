"""Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated
sequence. Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console. ET
1h """


def validate_input():
    while True:
        data = input(">>>Enter sequence (DO NOT enter STRING): ")
        _list = data.split(',')
        is_char = 0
        for element in _list:
            if element.isalpha():
                is_char += 1
        if is_char == 0:
            _list = list(map(str.strip, _list))
            return _list


def process_list(input_list):
    for binary in input_list:
        if int(binary, 2) % 5 == 0:
            print(binary, end=",")


def main():
    data = validate_input()
    process_list(data)


if __name__ == "__main__":
    main()