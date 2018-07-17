a = []
b = []
x = input("Do dai mang A: ")
y = input("Do dai mang B: ")

print("===========")
i = 0
while i<x:
	data = input("Nhap gia tri thu " + str(i+1) + ": ")
	a.append(data)
	i+=1
	
print("===========")
i = 0
while i<y:
	data = input("Nhap gia tri thu " + str(i+1) + ": ")
	b.append(data)
	i+=1

print("===========")
c = []
for each in a:
	for index in b:
		if index == each:
			c.append(index)

print("===========")
print(a)
print(b)
print(c)
