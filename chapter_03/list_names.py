guests = ['G1', 'G2', 'G3']
for guest in guests:
    print(f"You are invited {guest}")
print(f"{guests[0]} can't make it")
guests[0] = "New Guest"
print(guests)
for guest in guests:
    print(f"{guest} is invited finally")

print("**************************************")
for guest in guests:
    print(f"{guest} - we got a bigger table")

# Add a new guest
guests.insert(0,"Ankur")
print(guests)
guests.insert(int(len(guests)/2),"Manoj")
print(guests)
guests.append("Akhil")
print(guests)

for guest in guests:
    print(f"{guest} - only 2 people can come")

while(len(guests) != 2):
    guest_popped = guests.pop()
    print(f"{guest_popped} is removed from the list")

print(guests)

del guests[1]
del guests[0]
print(guests)