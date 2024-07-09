#empty list to store the pets in.
pets = []

#store each individual pets in one list.
pet = {
    'animal type': 'dog',
    'name': 'nala',
    'owner': 'riri',
    'weight': 8,
    'eats': 'chicken',
}
pets.append(pet)

pet = {
    'animal type': 'bird',
    'name': 'peng',
    'owner': 'jennifer',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'gato',
    'owner': 'emmanuel',
    'weight': 10,
    'eats': 'fish',
}
pets.append(pet)

#info about each pet
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
        
