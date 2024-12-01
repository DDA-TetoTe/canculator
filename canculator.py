import math

# Функции для выполнения операций
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка! Деление на ноль."

def percent(x, y):
    return (x / 100) * y

def stepen(x, y):
    return math.pow(x,y)


# Основная логика калькулятора
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Проценты (x% от y)")
print("6. Возведение в степень")

# Ввод выбора пользователя
choice = input("Введите номер операции (1/2/3/4/5/6): ")

# Ввод чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Выполнение выбранной операции
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
elif choice == '5':
    print(f"{num1}% от {num2} = {percent(num1, num2)}")
elif choice == "6":
    print(f"Выводим {num1} в степень {num2} = {percent(num1, num2)}")
else:
    print("Неверный ввод! Пожалуйста, выберите операцию из списка.")
