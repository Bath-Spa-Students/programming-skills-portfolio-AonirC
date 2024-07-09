#theater charges different ticket prices depending on a person's age
user_age = "how old are you?"
user_age += "\nenter 'quit' when you are finished. "

#user type "quit" to end loop
while True:
    age = input(user_age)
    if age == 'quit':
        break
    age = int(age)

#under 3 years
    if age < 3:
        print("  your entrance is free!")
#between 3 and 12 years
    elif age < 11:
        print("  your ticket is $10.")
#over 12 years
    else:
        print("  your ticket is $15.")
