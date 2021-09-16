kidaray=[21,6,9]

if kidaray[0]>kidaray[1]:
    if kidaray[0]>kidaray[2]:
        print(kidaray[0])
    else:
        print(kidaray[2])
else:
    if kidaray[1]>kidaray[2]        :
        print(kidaray[1])
    else:
        print(kidaray[2])
    
print(".........................")
kidarayBig=[21,6,9,122,4,45,35,3,234,23,23,3345,33,443]

max = 0
for x in kidarayBig:
    if x > max:
     max = x
    
print(max)