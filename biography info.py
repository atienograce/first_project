import re

p = re.compile('[a-zA-Z]+')
bio_info = input('Enter your name\n')
m = p.match(bio_info)

if m:
    print("Invalid name")
else:
    birth = input('Enter your date of birth\n')
    address = input('Enter your address\n')
    goals = input('Enter your personal goal\n')
    print(f'Name: {bio_info}\n'
          f'DoB: {birth}\n'
          f'Address: {address}\n'
          f'Goal: {goals}')
