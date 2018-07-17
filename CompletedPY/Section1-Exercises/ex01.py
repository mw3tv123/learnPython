# coding=utf-8
"""
In màn hình các số nguyên từ 1 đến 100, nhưng với bội của 3, in ra chữ “Fizz”
thay vì số đo. Với bội của 5, in ra chữ “Buzz” thay vì số đó. Với các số là bội
của cả 3 và 5 thì in ra chữ “FizzBuzz” thay vì số đó. Các số còn lại thì in ra
bình thưòng.

OUTPUT
1
2
Fizz
4
Buzz
...

Please solve this problem by using both `for condition` and `list comprehension`

Estimated time: 30 minutes
"""
# For condition
for_list = []
print("========== This is for_list =========")
for num in range(1,101):
    if num % 3 == 0:
        for_list.append('Fizz')
    elif num % 5 == 0:
        for_list.append('Buzz')
    else:
        for_list.append(num)
    print(for_list[num-1])
# List comprehension
print("========== This is comprehension_list =========")
comprehension_list = [num for num in for_list]
print(comprehension_list)
