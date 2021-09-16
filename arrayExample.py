


x = 10
name1 = "manoj"
name2 = "anuj"
name3 = "bittu"
#print(name1)


def mylen(arr):
    count = 0 ;
    for x in arr:       
        count = count +1
    return count

listOfNames = ["manoj", "anuj", "bittu", "atharv", "rp.prasad", "Shashi", "nirmala","mmm","dfdfdf"]

for x in listOfNames:       
    print(x)
    
for x in range(5):
    print(x)
    

#print(listOfNames[5])

r = myhjkllen(listOfNames)

print(".....",r)

for x in range( r ):
    print(listOfNames[x])
