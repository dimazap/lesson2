def get_summ(num_one, num_two):
	try:
		num_one = int(num_one)
		num_two = int(num_two)
		summ = num_one + num_two
		print(summ)
	except(ValueError):
		print("Убедись, что вставляешь в функцию цифры")

get_summ("cola", 3)