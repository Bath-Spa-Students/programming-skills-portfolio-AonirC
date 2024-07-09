#three major rivers and the country each river runs through. One key-value pair might be 'nile' : 'egypt'. *
rivers = {
    'nile': 'egypt',
    'yellow': 'china',
    'sepik': 'new guinea',
    'ganges': 'india',
    'zambezi': 'africa',
    }

#loop to print a sentence about each river, such as the nile runs through egypt
for river, country in rivers.items():
    print("The " + "river " + river.title() + "is in " + country.title() + ".")

#loop to print the name of each river included in the dictionary
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

#loop to print the name of each country included in the dictionary
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())
