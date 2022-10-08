
print('Щоб запустити калькулятор введіть 2 числа і дію')
number1=float(input("Введіть перше число: "))
number2=float(input("Введіть друге число: "))
rule=input("Ввеедіть дію: ")
if rule == "/" and number2==0:
    print("Ділення на нуль")
if rule == "+":
    print(number1+number2)
elif rule =="-":
    print(number1-number2)
elif rule =="*":
    print(number1*number2)
elif rule =="/":
    print(number1/number2)
else:
    print("Введіть правильну дію")

