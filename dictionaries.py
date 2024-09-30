"""
dictionaries are used to store data in key values pair. dictionaries are changeable ordered data collections.
"""

dict = {
    "name": "Zeeshan",
    "email": "zeeshan.it58@gmail.com",
    "district": "FSD"
}

#print(dict.items())
#Adding new items
dict["job"] = "SSE"

#print(dict)

#now try to change the item from dictionary
dict["name"] = "Zeeshan Ali"

#looping the dictionary
for x in dict:
    print(x) #this will print key by default

for x in dict.keys():
    print(x) #this will print keys only

for x in dict.values():
    print(x) #this will print keys

for x,y in dict.items():
    print(f"{x}:{y}") #this will print key and value