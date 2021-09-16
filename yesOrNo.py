array=[2,10,0,4,0,0,45]

FlagYesFound = False

for x in array:
    if x==0:
       FlagYesFound = True
       print("yes")
       break


if  FlagYesFound==False:
    print("no")           
