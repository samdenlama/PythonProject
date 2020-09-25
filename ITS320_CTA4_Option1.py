
index = 0
total = 0
average = 0
userInputs = []
while index < 5:
  userInput = float(input("Enter a number: "))
  total += userInput
  average = total/5
  userInputs.append(str(userInput))
  amountWithInterest = userInput + userInput * 0.2
  print("Amount with interest: " + str(amountWithInterest))
  index += 1  
print("The total is: " + str(total))
print("The average is: " + str(average))
print("The maximum value is: " + max(userInputs))
print("The minimum value is: " +  min(userInputs))

#Output
#Enter a number: 10
#Amount with interest: 12.0
#Enter a number: 20
#Amount with interest: 24.0
#Enter a number: 30
#Amount with interest: 36.0
#Enter a number: 40Amount with interest: 48.0
#Enter a number: 50
#Amount with interest: 60.0
#The total is: 150.0
#The average is: 30.0
#The maximum value is: 50.0
#The minimum value is: 10.0
