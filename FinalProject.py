import os.path

automobileContainer = []

class automobile:

  def __init__(self):
    self.__index = ""
    self.__make = ""
    self.__model = ""
    self.__color = ""
    self.__year = 0
    self.__mileage = 0

  def setIndex(self, index):
    self.__index = index
  def getIndex(self):
    return self.__index 
  def setMake(self,make):
    self.__make = make
  def getMake(self):
    return self.__make
  def setModel(self,model):
    self.__model = model
  def getModel(self):
    return self.__model
  def setColor(self,color):
    self.__color = color
  def getColor(self):
    return self.__color
  def setYear(self,year):
    self.__year = year
  def getYear(self):
    return self.__year
  def setMileage(self,mileage):
    self.__mileage=mileage
  def getMileage(self):
    return self.__mileage
  
  def printCurrentInventory(self):
    print("\nCurrent Inventory: \n")
    print("Index Make Model Color Year Mileage")
    for autoMob in automobileContainer:
      print(str(autoMob.getIndex())+" "+autoMob.getMake()+" "+autoMob.getModel()+" "+autoMob.getColor()+" "+str(autoMob.getYear())+" "+str(autoMob.getMileage()))
    print("\n")

  def addAutomobile(self):
    automobileContainer.append(self)

  def removeAutomobile(self,index):
    try:
      del automobileContainer[index]
    except IndexError:
      print("\nInvalid index used. Please try again.\n")
    for i in range(index,len(automobileContainer)):
      automobileContainer[i].__index =  automobileContainer[i].__index - 1

  def updateAutomobile(self,index):
    try:
      automobileContainer[self.__index]=self
    except IndexError:
      print("\nInvalid index used. Please try again.\n")

def endProgram():
  if len(automobileContainer)<1:
    print("Inventory is empty! No text file generated.")
  else:
    f = open("C:/Python/AutomobileInventory.txt","w+")
    f.write("Automobile Inventory\nIndex Make Model Color Year Mileage\n")
    for automobile in automobileContainer:
      f.write(str(automobile.getIndex())+" "+automobile.getMake()+" "+automobile.getModel()+" "+automobile.getColor()+" "+str(automobile.getYear())+" "+str(automobile.getMileage())+"\n")
    f.close()

def main():
  userSelection = 0
  while userSelection != '4':
    print("Welcome to Automobile Inventory Application\n")
    print("Please select the options below: \n")
    print("-Enter 1 to add an automobile\n-Enter 2 to remove an automobile\n-Enter 3 to update an automobile\n-Enter 4 to generate text file\n")
    userSelection = str(input())
    if userSelection == '1':
      print("Add an automobile")
      autoMobile = automobile()
      autoMobile.setMake(str(input("Please enter the automobile make: \n")))
      autoMobile.setModel(str(input("Please enter the automobile make: \n")))
      autoMobile.setColor(str(input("Please enter the automobile color: \n")))
      while True:
        try:
          autoMobile.setYear(int(input("Please enter the automobile year: \n")))
          break
        except ValueError:
          print("Year should be an integer")
      while True:
        try:
          autoMobile.setMileage(int(input("Please enter the automobile mileage: \n")))
          break
        except ValueError:
          print("Mileage should be an integer")
      autoMobile.setIndex(len(automobileContainer))
      autoMobile.addAutomobile()
      print("Automobile added successfully!")
      autoMobile.printCurrentInventory()
    elif userSelection == '2':
      print("Remove an automobile")
      if len(automobileContainer)<1:
        print("\nThere are no automobiles in the invetory to delete\n")
      else:
        print("Enter the index number of the automobile to remove.")
        try:
          index = int(input())
          autoMobile = automobile()
          autoMobile.removeAutomobile(index)
          print("\nAutomobile Removed Successfully!\n")
          autoMobile.printCurrentInventory()
        except ValueError:
          print("Invalid input index must be integer!\n")
    elif userSelection == '3':
      print("Update an automobile")
      if len(automobileContainer)<1:
        print("\nThere are no automobiles in the invetory to update\n")
      else:
        print("\nEnter the index number of the automobile to update.\n")
        while True:
          try:
            index = int(input())
            automobileContainer[index]
            break
          except ValueError:
            print("Index needs to be an integer")
          except IndexError:
            print("Invalid index. Please try again!")
        autoMobile = automobile()
        autoMobile.setMake(str(input("Please enter the new make: \n")))
        autoMobile.setModel(str(input("Please enter the new model: \n")))
        autoMobile.setColor(str(input("Please enter the new color: \n")))
        while True:
          try:
            autoMobile.setYear(int(input("Please enter the new year: \n")))
            break
          except ValueError:
            print("Year should be an integer")
        while True:
          try:
            autoMobile.setMileage(int(input("Please enter the new mileage: \n"))) 
            break
          except ValueError:
            print("Mileage should be an integer")       
        autoMobile.setIndex(index)
        autoMobile.updateAutomobile(index)
        print("Automobile updated successfully")
        autoMobile.printCurrentInventory()
    elif userSelection == '4':
      endProgram()

main()

