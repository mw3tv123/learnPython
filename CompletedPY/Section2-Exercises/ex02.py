"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
ET 30m
"""


class MyString:
    """Simple string method"""

    def __init__(self, string):
        self.string = string

    def getString(self):
        self.string = input(">>> Enter a string: ")

    def printString(self):
        return self.string.capitalize()

    def testCase(self):



if __name__ == "__main__":
    s = MyString()
    s.getString()
    print(s.printString())
