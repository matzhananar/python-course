numb1 = int(input("Введите первое число: "))
symbol = input("Введите символ: ")
numb2 = int(input("Введите второе число: "))

if symbol == '+':
    print("Ответ:",numb1+numb2)
elif symbol == "-":
    print("Ответ:",numb1-numb2)
elif symbol == "*":
    print("Ответ:",numb1*numb2)
elif symbol == "/":
    print("Ответ:",numb1/numb2)
elif symbol == "**":
    print("Ответ:",numb1**numb2)
elif symbol == "%":
    print("Ответ:",numb1*(numb2/100))
else:
    print("введите правильный символ")



