"""Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then,
the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98') ET 30m """


def handle_input():
    while True:
        data = input(">>>Enter your number sequence (DO NOT enter STRING): ")
        _list = data.split(',')
        is_char = 0
        for element in _list:
            if element.isalpha():
                is_char += 1
        if is_char == 0:
            break
    _list = list(map(str.strip, _list))
    _tuple = tuple(_list)
    return _list, _tuple


def main():
    my_list, my_tuple = handle_input()
    print("{0} {1}".format(my_list, my_tuple))


if __name__ == "__main__":
    main()