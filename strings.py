line1 = 9
line2 = "learn"

if type(line1) is not str or type(line2) is not str:
	print(0)
elif line1 == line2:
	print(1)
elif len(line1) > len(line2):
	print(2)
elif line2 == 'learn':
	print(3)
else:
	print('fix your code')