try:
    number = int(input("What are you thinking of? "))
except ValueError:
    print("Enter appropriate value")

if (number % 2) == 0:
    print("It's an even number")
else:
    print("It's an odd number") 