import random
import time

Operators = ["+","-","*"]
min_operand = 3
max_operand = 12
total_problems = 10

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(Operators)

    expr = str(left) + " " + operator + " " + str(right)    
    answer = eval(expr)
    # print(expr,"=", answer)
    return expr, answer

wrong = 0
input("Press 'Enter' to start!\n")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem#" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            print("Correct!")
            break
        print("Wrong!")
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("\nNice work! You finished in", total_time, "seconds and made", wrong,"mistakes!\n")