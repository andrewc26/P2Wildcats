import json as j

# initial family dictionary
family_dict = {
    "p1": {
        "firstname": "Andrew",
        "lastname": "Crisostomo",
        "age": 17,
        "gender": "male"
    },
    "p2": {
        "firstname": "Lauren",
        "lastname": "Crisostomo",
        "age": 18,
        "gender": "female"
    },
    "p3":  {
        "firstname": "Ryan",
        "lastname": "Crisostomo",
        "age": 13,
        "gender": "male"
    },
    "p4": {
        "firstname": "Mark",
        "lastname": "Crisostomo",
        "age": 45,
        "gender": "male"
    }
}

family_list = []

# turning dictionary into list with for loop
for i in range(0, 4):
    family_list.append(family_dict.get(f"p{i + 1}"))

print(family_list)

# converting list to dictionary
family = {
    "p1": dict(family_list[0].items()),
    "p2": dict(family_list[1].items()),
    "p3": dict(family_list[2].items()),
    "p4": dict(family_list[3].items())
}

print("\n\n\n")

print(f"family dictionary: {family}")

json_data = j.dumps(family, indent=4)

f = open("out.json", "w+")
f.write(json_data)
f.close()  # writing family dictionary to file out.json

# printing out contents of json file
x = j.load(open("out.json"))

extended_fam = {
    "p5": {
        "firstname": "Tommy",
        "lastname": "Alo",
        "age": 90,
        "gender": "male"
    },
    "p6": {
        "firstname": "Emilita",
        "lastname": "Alo",
        "age": 74,
        "gender": "female"
    },
}

x.update(extended_fam)

print(x)

print("\n\n\n")

print("printing from json file: ")

for i in range(1, 7):
    print("$$$$$$$$$$$$$")
    print(x.get(f"p{i}"))
    print("$$$$$$$$$$$$$")

print("\n\n\n")

some_dict = {
    "family": x
}

# printing out family members
for i in range(1, 7):
    print(some_dict.get("family").get(f"p{i}"))