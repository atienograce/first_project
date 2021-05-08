phone_number = input('What is your phone number? ')
digit_mapping = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output = ""
for ch in phone_number:
    output += digit_mapping.get(ch, "!") + " "
print(output)