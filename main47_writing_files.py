# Writing files - txt, json, csv

txt_data = "I like greatfuits!"

file_path = "python/modules/output.txt"
try:
    with open(file=file_path, mode="x") as file:                              # w - for write, x - for write if file doen't exists already, a - for append (beveik w = x + a)
        file.write(txt_data + "\n")
        print(f"txt file '{file_path}' was created!")
except FileExistsError:
    print("That TXT file already exists!")

import json
file_path2 = "python/modules/output.json"

employee = {
    "name": "Spongebob",
    "age": 30,
    "position": "cook"
}

try:
    with open(file_path2, "x") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path2}' was created")
except FileExistsError:
    print("That JSON file already exists!")

import csv
file_path3 = "python/modules/output.csv"


employees = [["Name", "Age", "Position"],
             ["Spongeobo", 30, "Cook"],
             ["Patrick", 37, "Cashier"],
             ["Garry", 3, "Pet"]]

try:
    with open(file_path3, "x", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path3}' was created")
except FileExistsError:
    print("That CSV file already exists!")