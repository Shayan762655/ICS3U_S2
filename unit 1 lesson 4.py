# Predict
# I predict that the code will print Please input a whole number: and wait for the user to input something into the console
# It will then print When (the number entered by the user)  is divided by 6 the result is: (result of the number divided by 6)
# For example if I input the number 12, it will output:
# Please input a whole number:  12
# When 12  is divided by 6 the result is: 2.

# Run
# my prediciton was correct

#inspect
# It stopped execution because of the use of input () in the code 
# It waits until the user inputs somehting into the console

# Modify
Num = input("Please input a whole number: ")
Num3 = input("Use any whole number except 0: ')
num = int(num)
num3 = int(num3)
num2 = num / num3
print("When", num, "is divided by", num3, "the result is:", num2)
# The reason the instruction "Use any whole number except zero" is needed because you can't divide by 0
# It will cause python to crash
