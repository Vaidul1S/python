# Reading files - txt, json, csv

file_path1 = "python/modules/output.txt"

try:
    with open(file_path1, "r") as file:                                                 # r - for read
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File was not found!")
except PermissionError:
    print("You don't hahve permission to the file!")

import json

file_path2 = "python/modules/output.json"

try:
    with open(file_path2, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("File was not found!")
except PermissionError:
    print("You don't hahve permission to the file!")

import csv

file_path3 = "python/modules/output.csv"

try:
    with open(file_path3, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
        print(content)
except FileNotFoundError:
    print("File was not found!")
except PermissionError:
    print("You don't hahve permission to the file!")