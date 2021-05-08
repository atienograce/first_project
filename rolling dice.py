import random

while True:
    print('Roll dice...')
    print(f'The value is', random.randint(1,6))
    repeat = input("Continue with game? 'y' for yes and 'n' for no: ")
    if repeat == 'n':
        print("game over")
        break