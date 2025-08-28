# 2d List - list of list
# galibuti is set of sets, tuple of tuples arba misrus pvp tuple of list or sets

# fruits = ["apple", "pear", "orange", "greatfruit"]
# vegetables = ["celery", "letus", "carrot", "potato"]
# meats = ["chicken", "port", "beef", "lamb"]

# groceries = [fruits, vegetables, meats]

groceries = [["apple", "pear", "orange", "greatfruit"],
             ["celery", "letus", "carrot", "potato"],
             ["chicken", "port", "beef", "lamb"]]

print(groceries)
print(groceries[0])
print(groceries[1][3])

for collection in groceries:
    for item in collection:
        print(item, end = " ")
    print()


# exercise tuple of tuples

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()