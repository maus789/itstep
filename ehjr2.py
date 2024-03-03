#1#
ім_я = input("Будь ласка, введіть ваше ім'я: ")
print("Привіт, " + ім_я + "! Вітаю вас!")
#2#
name = input("Будь ласка, введіть ваше ім'я: ")
age = 11
print("Привіт, " + name + "!")

if age > 18:
    print("Ти дорослий")
elif age == 18:
    print("Ти дорослий")
else:
#   print("Ти ще дитина")
#3#
number = float(input("Введіть число: "))

if number >= 0:
    print("Число без змін:", number)
else:
    print("Число з протилежним знаком:", -number)
#4#
correct_password = "589632147"

input_password = input("Введіть пароль: ")

if input_password == correct_password:
    print("Пароль вірний")
else:
    print("Пароль невірний, ти його забув хаха")
#5#
number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))
if number1 > number2:
    print("Більше число:", number1)
elif number2 > number1:
    print("Більше число:", number2)
else:
    print("Числа рівні")
#6#
number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))
number3 = float(input("Введіть третє число: "))

average = (number1 + number2 + number3) / 3

print("Середнє значення:", average)
#7#
length = float(input("Введіть довжину прямокутника: "))
width = float(input("Введіть ширину прямокутника: "))

area = length * width
perimeter = 2 * (length + width)

print("Площа прямокутника:", area)
print("Периметр прямокутника:", perimeter)
#8#
number = int(input("Введіть число від 1 до 7: "))

if number == 1:
    print("Понеділок")
elif number == 2:
    print("Вівторок")
elif number == 3:
    print("Середа")
elif number == 4:
    print("Четвер")
elif number == 5:
    print("П'ятниця")
elif number == 6:
    print("Субота")
elif number == 7:
    print("Неділя")
else:
    print("Введене число не відповідає жодному дню тижня")
#9#
number = int(input("Введіть число: "))

if number % 2 == 0:
    print("Число парне")
else:
    print("Число не парне")
#10#
def can_break_chocolate(n, m, k):
    total_pieces = n + m - 2
    if k >= 0 and k <= total_pieces:
        return True
    else:
        return False

n = int(input("Введіть кількість рядків шоколадки (n): "))
m = int(input("Введіть кількість стовпчиків шоколадки (m): "))
k = int(input("Введіть бажану кількість частинок (k): "))

if can_break_chocolate(n, m, k):
    print("Так, можливо отримати рівно", k, "частинок шоколадки.")
else:
    print("Ні, неможливо отримати рівно", k, "частинок шоколадки.")