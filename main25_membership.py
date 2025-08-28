# Membership operators - in, not in

word = "apple"

letter = input("Guess a letter on the hidden word: ")

if letter in word:
    print(f"There is a {letter}!")
else:
    print(f"{letter} was not found!")


students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student not in students:
    print(f"{student} was not found!")
else:
    print(f"There is {student} in a class!")


grades = {"Sandy": "A", 
          "Spongebob": "B",
          "Squidward": "C",
          "Patrick": "F"
          }

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found.")

email = "fake@email.com"

if "@" in email and "." in email:
    print(f"Valid email!")
else:
    print("Invalid email!")