import random
import string

def generate_password(L, A):
    # Визначення алфавіту залежно від значення A
    if A == 26:
        alphabet = string.ascii_lowercase  # тільки малі літери
    elif A == 52:
        alphabet = string.ascii_letters  # малі та великі літери
    elif A == 62:
        alphabet = string.ascii_letters + string.digits  # літери і цифри
    elif A == 94:
        alphabet = string.ascii_letters + string.digits + string.punctuation  # літери, цифри, спеціальні символи
    else:
        raise ValueError("Невірне значення A.")

    # Генерація пароля довжиною L
    password = ''.join(random.choice(alphabet) for _ in range(L))
    return password

# Введення параметрів користувачем
L = int(input("Введіть довжину пароля: "))
A = int(input("Введіть кількість символів в алфавіті (можна вибрати 26, 52, 62, 94): "))

# Перевірка введеного значення A
if A not in [26, 52, 62, 94]:
    print("Невірне значення A!")
else:
    # Генерація пароля
    password = generate_password(L, A)
    print(f"Згенерований пароль: {password}")
# hello
