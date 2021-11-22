# LIST AND EVERY ELEMENT IS A DICTIONARY
people = [
    {"name": "Hik HIk", "Age": "24"},
    {"name": "Hikal Hiker", "Age": "22"},
    {"name": "Test Tester", "Age": "22"},
    {"name": "Linkin PArk", "Age": "50"}
]

#teaching function sort how to sort ☝

def f(person):
    return person["name"]

#PASSING key as f()
people.sort(key=f)

print(people)
