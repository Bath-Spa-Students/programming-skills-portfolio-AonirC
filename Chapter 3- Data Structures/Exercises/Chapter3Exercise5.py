guests = ['Hanna Crisna', 'Mae Gallego', 'Darnelle Infantes']
name = guests[2].title()
print(f"\nSorry, {name} can't make it to the party.")

# Darnelle can't make it! Let's invite Therese instead.
del(guests[2])
guests.insert(1, 'Therese')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to the party.")

name = guests[1].title()
print(f"{name}, please come to the party.")

name = guests[2].title()
print(f"{name}, please come to the party.")
