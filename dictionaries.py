my_dict = {
    "321412": {
        "name": "John",
        "last": "Doe"
    },
    "341552": {
        "name": "Cathrine",
        "last": "Jones"
    }
}

for id, student in my_dict.items():
    print(student["name"], student["last"])