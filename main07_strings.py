# Strings

name = input("Please enter your name: ")

print(len(name))                            # ilgis
print(name.find(" "))                       # ieskom pirmo tarpo
print(name.rfind("l"))                      # ieskom paskutines "l"
print(name.capitalize())                    # pirmas zodis is didziosios
print(name.upper())                         # didziosios
print(name.lower())                         # mazosios
print(name.isdigit())                       # gaunam bool'i ar stringas susideda tik is skaiciu
print(name.isalpha())                       # gaunam bool'i ar stringas susideda tik is abc raidziu ir be tarpu

phone = "123-456-7890"

print(phone.count("-"))                     # skaiciuojam -
print(phone.replace("-", " "))              # keiciam - i tarpus

# validation exercise

username = input("Enter username: ")

if len(username) > 12:
    print("Username can't be longer than 12 characters!")
elif username.find(" ") > 0:
    print("Username can't contain spaces!")
elif not username.isalpha():
    print("Use letters only no numbers!")
else:
    print(f"Welcome {username}.")