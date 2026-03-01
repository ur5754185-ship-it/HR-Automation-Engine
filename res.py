import csv

with open("data.csv", newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print("Name:", row["name"])
        print("Skills:", row["skills"])
        print("Experience:", row["experience"])
        print("-----------")