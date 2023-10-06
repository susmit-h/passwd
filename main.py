import random

password = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@!#$%^&*()_+-~?=|\/:;"'<>'.'''
length = int(input('Enter the length of the password: '))

random_password = random.sample(password,length)
final_password = "".join(random_password)

print(f"Your password is {final_password}")
