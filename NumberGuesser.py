import random
def start():
    print("I'm thinking of a number between one and ten...")
start()

def guess(): #start number guess here

    #Randomize number
    correctNumber = random.randint(1,10)

    while True:
        playerGuess = input("What do you think it is? ")
        try:
            if int(float(playerGuess)) >=11:
                print("That's a bit higher than I was thinking, try again.")
                continue
            if int(float(playerGuess)) <=0:
                print("That seems a bit low. Give it another shot.")
            elif int(float(playerGuess)) == int(float(correctNumber)):
                print("That's it!")
                def replay(): #ask to replay or quit
                    yesNo = input("Would you like to play again? ")
                    if str.lower(yesNo) == 'yes':
                        print("Okay. I'm thinking of another number between one and ten.")
                        guess()
                    elif str.lower(yesNo) == 'no':
                        print("Okay well thanks for playing!")
                        exit()
                    else:
                        print("Uh... That wasn't yes or no. Try again.")
                        replay()
                replay()
            if int(float(playerGuess)) != int(float(correctNumber)):
                print("Sorry, try again.")
                continue
            else: #Not sure what could cause this to get used, but it doesn't hurt to have an "unexpected error occured" message.
                print("I'm not quite sure what just happened, but something broke. Let's try that again.")
                continue
        except ValueError: #Should handle all unexpected integers or strings.
            print("That might not have been a number. Please try 1-10")
guess()
