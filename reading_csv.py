import csv

user_input = input("File to open: ")

with open(user_input, mode = 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)