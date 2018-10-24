#Parker Dean
#10/11/18


print("You are walking through the woods when you come across a giant beast.")
print("As soon as he makes eye contact with you, he yells and runs at you.")
print("You look down at your sword and know you only have 2 options.")
import random
win = 0
mHealth = 100
pHealth = 100
fight = 1
choice = "attack"
choice = input("Do you want to attack or run?: ")
while fight == 1 :
    
    if choice == "attack":
        playerDamage = random.randrange(0, 25)
        monsterDamage = random.randrange(0, 30)
        print("You attacked the monster for",playerDamage)
        mHealth -= playerDamage
        if mHealth > 0:
            print("The monster attacked you for ", monsterDamage)
            pHealth -=  monsterDamage
        if pHealth <= 0:
            win = 0
            print("You got bitch slapped." )
            break
        elif mHealth <= 0:
            win = 1
            print("You stabbed your sword through the monster's heart and it flopped over and died!")
            break
        elif pHealth >= 0 and mHealth >= 0:
            print ("You have ", pHealth, "health  left.")
            print ("The monster has",mHealth, "health left.")
            choice= input("attack or run ")
    else:
        fight = 0
        choice = "run"
        print("You are a coward")
        win == 0
        break


    
if  win == 0: 
    print("Game Over")
else:
    print("You Win!")
