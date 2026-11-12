guests = input("Enter the people u wanna invite: ")
with open ("guest.txt",'a') as f:
    f.write(guests + "\n")

print()
print(" 🎉 Guest List 🎉 ")
count = 0
with open("guest.txt", 'r') as f:
    for line in f :
        count += 1
        print(count,line.strip())

print("Total Guests: ", count)


who = input("search for the name: ")
found = False 

with open("guest.txt", 'r') as f:
    for line in f:
        if who == line.strip():
            found = True 
if found :
    print(who,"is invited")
else:
    print(who,"is not on the list")
