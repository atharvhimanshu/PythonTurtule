#sGameover = false


aray = [111,111,554,777,896,666,564]


score = 0
health = 3

for i in aray:
    if i>300 and i<600:
        print(i)




while True:
    uinput = input()
    if uinput == "a":
        score = score + 1
        print("Score ",score)

    if uinput == "f":    
        health = health - 1
        if health > -1:
            print("Health ",health)

    if health<1:
       # print("GAME OVER")

  