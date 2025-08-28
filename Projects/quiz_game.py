print("Welcome to the quiz game!")

playing = input("Do you want to play?(Yes/No) ")

if playing.lower() != "yes":
    print("Maybe other time then :)")
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
else: 
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
else: 
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
else: 
    print("Incorrect!")

answer = input("What does PU stand for? ")
if answer.lower() == "power unit":
    print("Correct!")
else: 
    print("Incorrect!")