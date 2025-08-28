# List Comprehension

doubles1 = []

for x in range(1, 11):
    doubles1.append(x * 2)

print(doubles1)
print()

doubles2 = [x * 2 for x in range(1, 11)]

print(doubles2)
print()

triples = [y * 3 for y in range(1, 11)]

print(triples)
print()

fruits = ["pineapple", "orange", "banana", "peach"]
fruits = [fruit.capitalize() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]

print(fruits)
print(fruit_chars)

numbers = [1,-2,3,-4,5,6,7,-8,-9,10]   

positive_numbs = [num for num in numbers if num>= 0]
negative_numbs = [num for num in numbers if num<= 0]
even_numbs = [num for num in numbers if num % 2 == 0]
odd_numbs = [num for num in numbers if num % 2 != 0]

print(positive_numbs)
print(negative_numbs)
print(even_numbs)
print(odd_numbs)

grades = [85,42,79,90,56,64,30,25]

passing_grades = [grade for grade in grades if grade >=60]

print(passing_grades)