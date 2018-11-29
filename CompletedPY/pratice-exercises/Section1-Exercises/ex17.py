"""You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian
folk art based on creation of patterns.) Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in
alphabetical order).

Input Format
Only one line of input containing N, the size of the rangoli.

Output Format
Print the alphabet rangoli in the format explained above.

Sample Input
5

Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

ET: 4 hours
"""

# Old code
def rangoli_with_while(n):
    i = 0
    while i < n*2-1:
        j = 0
        if i < n-1:
            while j < n*2-1:
                if j < n:
                    if j >= n-i-1:
                        print("*", end=" ")
                    else:
                        print("-", end=" ")
                elif j == n-1:
                    print("*", end=" ")
                else:
                    if j <= n+i-1:
                        print("*", end=" ")
                    else:
                        print("-", end=" ")
                j += 1
        elif i < n:
            while j < n*2-1:
                print("*", end=" ")
                j += 1
        else:
            while j < n*2-1:
                if j < n:
                    if j <= i-n:
                        print("-", end=" ")
                    else:
                        print("*", end=" ")
                elif j == n // 2 + 2:
                    print("*", end=" ")
                else:
                    if j > n*3-i-3:  # Not work with n < 5
                        print("-", end=" ")
                    else:
                        print("*", end=" ")
                j += 1
        print()
        i += 1


# New code
def rangoli_with_for(n):
    for i in range(0, n*2-1):
        for j in range(0, n*2-1):
            if i < n:
                if n-i-1 <= j <= n+i-1:
                    print("*", end=" ")
                else:
                    print("-", end=" ")
            else:
                if i-n+1 <= j <= n*3-i-3:
                    print("*", end=" ")
                else:
                    print("-", end=" ")
        print()


def main():
    n = int(input(">>>Enter your number: "))
    rangoli_with_while(n)
    print("= "*n*2)
    rangoli_with_for(n)


main()
