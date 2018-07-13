import datetime

# Feature #
def calPlus():
	getData();
	return a+b

def calMinus():
	getData();
	return a-b

def calDivide():
	getData()
	try: return a//b
	except ZeroDivisionError as err:
		errDetail = str(err)
		print("Error: " + errDetail)

def calMulti():
	getData()
	return a*b

# Get Data from User #
def getData():
	try:
		global a, b
		a = input("\n+Nhap a: ")
		b = input("+Nhap b: ")
	except TypeError as err:
		errDetail = str(err)
		print("Loi: " + errDetail)

# Save to file #
def saveLog(contents = " "):
	with open("log.txt", "at") as f:
		x = str(datetime.datetime.now())
		x += "\n" + contents
		f.write(x)
		
# Read data from file #
#def readData(path = "")
#	with open(path, "rt") as f:
#		return f

# Login from File's Data #
def logingData(usern = "", passwd = ""):
	with open("userdata.txt", "rt") as data:
		for line in data:
			user = line.split(' ')
			name = user[0]
			pawd = user[1]
			if name.startswith(usern) and pawd.startswith(passwd):
				return true
			return false

# Menu UI #
def menu():
	print("=======================")
	print("May tinh".center(20))
	print("(1)Cong")
	print("(2)Tru")
	print("(3)Chia")
	print("(4)Nhan")
	print("(5)Thoat")

# Initial variables
count = 0
log = ""

# Main #
print(">>Ten dang nhap: ")
uname = input()
print(">>Mat khau: ")
upawd = input()
if logingData(uname, upawd):
	while True:
		count += 1
		menu()
		mode = input("#Chon tinh nang (1~5): ")
	
		if mode==1:
			result = calPlus()
			log += "(+)\t\t"
		elif mode==2:
			result = calMinus()
			log += "(-)\t\t"
		elif mode==3:
			result = calDivide()
			log += "(/)\t\t"
		elif mode==4:
			result = calMulti()
			log += "(*)\t\t"
		else:
			saveLog(str(log))
			break
	
		log += "Lan {0:2s}:\ta={1:4s}\tb={2:4s}".format(str(count), str(a), str(b))
		log += " ==> KQ={0:4s}\n".format(str(result))
	
		print("==>Ket qua: " + str(result))
else:
	print "Sai thong tin dang nhap"
