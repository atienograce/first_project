email = input("What is your email address? ").strip()
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
print(f"Hey {username},I see your email is registered with {domain}.That's cool!")