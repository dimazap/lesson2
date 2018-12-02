age = int(input("What is your age? "))
print(f"You are {age} years old")

def check_age(age):
	if age in range(0, 7):
		print('Hi, you are in kindergarden')
	elif age in range(7, 19):
		print('Hi, you are a pupil')
	elif age in range(19, 25):
		print('Hi, you are a student')
	else:
		print('Hi, you are a worker')

check_age(age)