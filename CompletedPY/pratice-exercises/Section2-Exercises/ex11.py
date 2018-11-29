"""
Write a function that sorts a list.
The user should be able to pass a compare function that determines
the order of 2 elements in the list.

Example:
def sort(list, comp):
    # TODO: Place your code here, return sorted list.
    pass

def less(a, b):
    return a < b

def greater(a, b):
    return a > b

l = [1, 2, 9, 8, 5, 6]
print(sort(l, less))
print(sort(l, greater))

ET: 2 hours
"""


# Sort this input list base on compare method
def sort(list, comp):
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if comp(list[i], list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list


def less(a, b):
    return a < b


def greater(a, b):
    return a > b


def validate_input():
    # Validate list input
    while True:
        n = input(">>> Enter the number of elenment: ")
        if n.isdigit():
            for i in range(n):
                while True:
                    usr_element = input(">>> Enter number: ")
                    if not usr_element.isalpha():
                        break  # Hadouken code :)
                valid_list.append(usr_element)
            break
    # Validate compare method user choose
    while True:
        option = ['less', 'greater', 1, 2]
        print("\t(1)Less\t(2)Greater")
        valid_comp = str.lower(input(">>> Enter compare name: "))
        if valid_comp not in option:
            continue
        break
    return valid_list, valid_comp


def main():
    usr_list, comp_func = validate_input()
    sort(usr_list, comp_func)


if __name__ == "__main__":
    main()