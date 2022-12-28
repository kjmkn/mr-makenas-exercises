i = 0
while i != 100:
    i = i+1
    if i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print ('FizzBuzz')
        # Hint: Move to top for better results
    else:
        print (i)