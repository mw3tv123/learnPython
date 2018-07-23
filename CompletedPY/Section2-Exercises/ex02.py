"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
ET 30m
"""


class MyString:

    string = ""

    def getString(self):
        self.string = input(">>> Enter a string: ")

    def printString(self):
        print(self.string.capitalize())


def test_case():
    s = MyString()
    s.getString()
    s.printString()


if __name__ == "__main__":
    test_case()
