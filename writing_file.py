
data = """
Testing Data, Gender: Male, Randomness

"""

with open("data.csv", "w") as file:
    file.write(data)
print(data)