mydict = {
    "dict1":{
        "name": "Zeeshan",
        "email": "zeeshan.it58@gmail.com",
        "age" : 28
    },
    "dict2":{
        "profession": "developer",
        "city": "Lahore",
        "designation": "SSE"
    }
}

for x, obj in mydict.items():
    for y in obj:
        print(obj[y])
#now we'll access this with loop