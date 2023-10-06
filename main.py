import random

password = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@!#$%^&*()_+-~?=|\/:;"'<>'.'''
length = int(input('Enter the length of the password: '))

random_password = random.sample(password,length)


print(f"Your password is {random_password}")
