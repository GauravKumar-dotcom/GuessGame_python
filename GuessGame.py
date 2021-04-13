#This is a number guessing game in python
A= 18 #This is our number
i= 0 #number to be used in loop
print ("You will get 9 chances to guess the number!")
while (i<9):
    i= i+1 #value of i will increase each time the loop continues by 1
    B= 9-i #this is for number of guesses left
    X= int(input ("Guess the number: "))
    if (X>18):
        print ("Your number is greater! Try again!!")
        print ("Number of guesses left: ",B)
        continue #this will go back to the loop if statement goes right
    elif (X<18):
        print ("You number is smaller! Try again!!")
        print ("Number of guesses left: ",B)
        continue
    if (X== 18): 
        print ("Congratulations! you have guessed the number!!!")
        print ("Number of gusses used: ",i)
        break #this will come out of the loop is statement is right   
