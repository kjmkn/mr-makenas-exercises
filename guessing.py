right = 8
tries = 3
# guess = int(input("Enter a number "))
while tries > 0:
    guess = int(input("Enter a number "))
    if guess == right:
        print ("Success")
        break
    else:
        difference = guess - tries
        if guess > right:
            print ("Your guess was higher than the actual number")
        elif guess < right:
            print ("Your guess was lower than the actual number")
        tries = tries - 1
        # print ("Please try again")
if tries == 0:
    print (f"Game over. The answer was {right}")
