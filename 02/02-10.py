num1 = float(input("Введите число: "))
num2 = float(input("Введите число: "))
q = input("Введите желаемое арифметические действие: ")
if q == "-":
   print(num1 - num2)

elif q == "+":
   print(num1 + num2)

elif q == "*":
   print(num1 * num2)

elif q == "/":
   if num2 != 0:
       print(num1 / num2)
   else:
       print(888888)
else:
   print(888888)