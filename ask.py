def main():
	talk = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Что будешь делать?": "Программировать"}
	while True:
		keyinput = input("Каков твой вопрос? ")
		if keyinput in talk.keys():
			print(talk[keyinput])
		else:
			print("Тогда до свиданья")

main()