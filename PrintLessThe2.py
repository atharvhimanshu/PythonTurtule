kidarayBig=[2,-1,9,2,4,5,5,3,-3,4,2,0,1,3]

count=0

for x in kidarayBig:
    if x < 2:
        print(x)
        count=count+1
        
print("-------total count of num less than 2-----",count)


print("-----------------------------------------------")
print("new website")

kidarayBig=[2,-1,9,2,9,5,5,6,-3,6,2,0,33,3]
sum=0
for x in kidarayBig:
    print(x)
    sum=sum+x
print("sum this all number up:",sum)


print("-----------------------------------------------")
for x in kidarayBig:
    #print(x)
    if x != 0:
        if x%4 == 0:
            print(x)