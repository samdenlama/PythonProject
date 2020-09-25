firstList = [1,2,3,10,11]
secondList = [7,8,11,23,8,12,88]

result = ""
count = 0
for x in firstList:
  if(count == 0):
    result += "["
  for y in secondList:
    count += 1
    if(count == len(firstList) * len(secondList)):
      result += "(" + str(x)+","+str(y)+")]"
    else:
      result += "(" + str(x)+","+str(y)+"),"

print("List A: "+ str(firstList))
print("List B: "+ str(secondList))
print("Cartesian Product: \n" + result)

#Result:
#List A: [1, 2, 3, 10, 11]
#List B: [7, 8, 11, 23, 8, 12, 88]
#Cartesian Product:[(1,7),(1,8),(1,11),(1,23),(1,8),(1,12),(1,88),
#(2,7),(2,8),(2,11),(2,23),(2,8),(2,12),(2,88),(3,7),(3,8),(3,11),
#(3,23),(3,8),(3,12),(3,88),(10,7),(10,8),(10,11),(10,23),(10,8),
#(10,12),(10,88),(11,7),(11,8),(11,11),(11,23),(11,8),(11,12),(11,88)]
