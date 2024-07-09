#if-elif-else chain of a person's stage of life
age = float(input("enter age: "))

if age < 2:
    print("You're a toddler!")
elif age < 12:
    print("You're a kid!")
elif age < 19:
    print("You're a teenager!")
elif age < 59:
    print("You're an adult!")
else:
    print("You're an elder!")
