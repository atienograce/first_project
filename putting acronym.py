message = input('> ')
words = message.split()
acronym_converter = {
    "As soon as possible":"ASAP",
    "World Health Organization":"WHO",
    "Absent Without Leave":"AWOL"
}
output=""
for word in words:
    output += acronym_converter.get(word, "!") + " "
print(output)