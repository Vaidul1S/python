from cryptography.fernet import Fernet

def load_key():
    file = open("python/Projects/key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


# def write_key():
#     key = Fernet.generate_key()
#     with open("python/Projects/key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()


def view():
    with open('python/Projects/password.txt', 'r') as f:
        for line in f.readlines():
           data = line.rstrip()
           user, pasw = data.split("|")                         #returns List
           print("User:", user, "Password:", fer.decrypt(pasw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('python/Projects/password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input('Would you like to add a new password or view existing ones (view, add), press q to quit? ').lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        break