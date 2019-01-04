#Parker Dean
#12-20-18
#Coin Flip

def coin_flip():
    import random

    flips = 0
    heads = 0
    tails = 0

    #Print out ascii art
    print("""
            _.-'~~`~~'-._
         .'`  B   E   R  `'.
        / I               T \\
      /`       .-'~"-.       `\\
     ; L      / `-    \\      Y ;
    ;        />  `.  -.|        ;
    |       /_     '-.__)       |
    |        |-  _.' \\ |        |
    ;        `~~;     \\\\        ;
     ;  INGODWE /      \\\\)P    ;
      \\  TRUST '.___.-'`"     /
       `\\                   /`
         '._   1 9 9 7   _.'
            `'-..,,,..-'`""")

    coin_guess = input("If i flip a coin 100 times, which do you think will be higher? Heads or Tails: ")
    while flips < 100:
        if random.randint(1,2) == 1:
            print("heads")
            heads += 1
        else:
            print("tails")
            tails += 1
        flips += 1
    if coin_guess.lower() == "heads":
        print("So you guessed Heads")
        print("There were" , heads , "Heads, and there were" , tails , "tails")
        if heads > tails:
            print("You Win!")
        else:
            print("You Lose!")
    elif coin_guess.lower() == "tails":
        print("So you guessed Heads")
        print("There were" , tails , "Tails, and" , heads , "Heads")
        if heads < tails:
            print("You Win!")
        else:
            print("You Lose!")

coin_flip()
