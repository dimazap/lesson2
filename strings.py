line1 = "eieieiieieei"
line2 = "learner"

if type(line1) is not str and type(line2) is not str :
	print(0)
elif line1 == line2 :
	print(1)
elif len(line1) >= len(line2) :
	print(2)
elif line1 != line2 and line2 == 'learn' :
	print(3)
else:
	print('fix your code')