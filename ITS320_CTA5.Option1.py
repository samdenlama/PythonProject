def reverseString(str):
    reverseInput = str[len(str)::-1]
    return reverseInput

def main():
    finalOutput = ""
    x = 0
    while x<3:
        userInput = input("Enter a string: ")
        finalOutput += reverseString(userInput)
        x+=1 
    print(finalOutput)

main()

#result
#Enter a string: Apple
#Enter a string: Oranges
#Enter a string: Peach
#elppAsegnarOhcaeP


