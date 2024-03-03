#ex1
def multiply(number):
    result = 1
    for i in number:
        result *= i
        
    return result
l = [1,3,4,5]
result = multiply(l)
print(result)

#ex2
word = str(input())
def string(word):
    upper = 0
    lower = 0
    for char in word:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print(upper, lower)
string(word)

#ex3
def is_palindrome(s):
    # Приводим строку к нижнему регистру и удаляем пробелы
    s = s.lower().replace(" ", "")
    
    # Сравниваем строку с её обратным порядком
    return s == s[::-1]

# Пример использования
input_string = input("Введите строку: ")
if is_palindrome(input_string):
    print("Это палиндром!")
else:
    print("Это не палиндром.")
#ex4
import time
import math

def square_root(x):
    return math.sqrt(x)

def delayed_square_root(x, delay_ms):
    time.sleep(delay_ms / 1000)  # Переводим миллисекунды в секунды и создаем задержку
    result = square_root(x)
    return result

# Пример использования
number_to_sqrt = 25
delay_milliseconds = 1000  # Задержка в миллисекундах (1 секунда)

result = delayed_square_root(number_to_sqrt, delay_milliseconds)
print(f"Квадратный корень из {number_to_sqrt} после {delay_milliseconds / 1000} секунд: {result}")
#ex5
tuple1 = (True, True, False)
tuple2 = (True, True, True)
print(all(tuple1))
print(all(tuple2))