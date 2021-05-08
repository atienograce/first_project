import random

user_input = int(input('Enter your password length: '))
input = "qwertyuiopasdfghjklzxcvbnm[]{}/?-+=><"
password = "".join(random.sample(input, user_input))
print(password)  