# Collection - List, Set, Tuple

# List [] - ordered and changeable, most flexible

fruits = ["pineapple", "orange", "banana", "peach"]

# print(help(fruits))                                               # all list commands

fruits.append("apple")                                              # prides gale
fruits.insert(3, "pear")                                            # prides pagal pasirinkta indeksa
fruits.sort()                                                       # pagal abs
fruits.reverse()                                                    # atvirkstine tvarka (ne pagal abc)


for x in fruits:
    print(x, end = " ")

print()
print("peach" in fruits)
print(fruits.index("apple"))
print(fruits.count("coconut"))

# Set {} - unordered, immutable, no duplicates. add/remove, no index

cars = {"ford", "audi", "bmw", "mercedes"}

cars.add("volkswagen")
cars.add("kia")
cars.remove("kia")
#cars.pop()                                                         # istrina viena
#cars.clear()                                                       # istrina viska

print(cars)

# Tuple () - ordered and unchangeable. Dublicates. Faster

brands = ("dior", "ysl", "coco", "celine", "lv")

print(brands)
print(brands.index("dior"))
print(brands.count("dior"))