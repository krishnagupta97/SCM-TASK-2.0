import random

#calculator code
def calculator():

    def addition(a,b):
        return a+b
    def substraction(a,b):
        return a-b
    def multiplication(a,b):
        return a*b
    def division(a,b):
        return a/b
    def average(a,b):
        return (a+b)/2
    def greatest_integer(a,b):
        return a//b

    print('''Choose any of the following Operation you to want to operate any two numbers:
    1) Addition
    2) Substraction
    3) Multiplication
    4) Division
    5) Floor Divsion''')

    ask=int(input("Type The Index of Operation: "))

    if(ask==1):
        print("'OKAY, so you are going with ADDITION'")
        print("Now Enter the Numbers You want to apply Operations")
        a=float(input("First number: "))
        b=float(input("Second number: "))
        add=addition(a,b)
        print('''processing....😉
      Hey, I got ! 🙂
        The addition of given Numbers is : ''',add)

    elif(ask==2):
        print("'OKAY, so you are going with SUBSTRACTION'")
        print("Now Enter the Numbers You want to apply Operations")
        a=float(input("First number: "))
        b=float(input("Second number: "))
        sub=substraction(a,b)
        print('''processing....😉
      Here is what you are waiting for ! 🙂
        The substraction of given Numbers is : ''',sub)

    elif(ask==3):
        print("'OKAY, so you are going with MULTIPLICATION'")
        print("Now Enter the Numbers You want to apply Operations")
        a=float(input("First number: "))
        b=float(input("Second number: "))
        mult=multiplication(a,b)
        print('''processing....😉
      Your Answer is almost here!
        The multiplication of given Numbers is : ''',mult)

    elif(ask==4):
        print("'OKAY, so you are going with DIVISION'")
        print("Now Enter the Numbers You want to apply Operations")
        a=float(input("First number: "))
        b=float(input("Second number: "))
        div=division(a,b)
        print('''processing....😉
      Your Answer is almost here ! 🙂
        The division of given Numbers is : ''',div)

    elif(ask==5):
        print("'OKAY, so you are going with FLOOR DIVISION'")
        print("Now Enter the Numbers You want to apply Operations")
        a=float(input("First number: "))
        b=float(input("Second number: "))
        floor=greatest_integer(a,b)
        print('''processing....😉
      Your Answer is almost here ! 🙂
        The floor division of given Numbers is :''',floor)
    else:
        print('''    ERROR......Sorry it can't be processed 😕''')
        
        
#random password generator,
def rpg():

    inp=[x for x in input("Enter the words space seperatedly for the password : ").split()]
    n=len(inp)

    result=""
    for x in range(n):
        data=random.randint(0,n-1)
        result=result+str(inp[data])

    print("|> Getting Your entered Keys         ")
    print("|> PROCESSING ON THE WAY.......      ")
    print("|> Loading.... Wait few seconds      ")
    print("|> Your Password: ",result)
    
    
#rock,paper,scissor
def rps():
    main=["ROCK","PAPER","SCISSOR"]
    print("Hey buddy Welcome Here, Let's have some fun Together 🤖")
    print("In case You want to exit the game you need to type - 'exit' ")
    print("Just choose one from |>> ",main)
    
    while True:
        ask = input("It's Your Turn : ").upper()
        if(ask=="EXIT"):
            break

        system=random.randint(0,2)
    
        if(system==0):
            x=main[0]
            print("So, Here is my move : ", x)
        elif(system==1):
            x=main[1]
            print("So, Here is my move : ", x)
        else:
            x=main[2]
            print("So, Here is my move : ", x)
        
        if(x==ask):
            print('''MATCH DRAWN,
                  Let's Have another Round 😉''')
        elif(x=="ROCK" and ask=="SCISSOR"):
            print('''YOU LOST,
                  Better Luck Next Time 🙃''')
        elif(x=="ROCK" and ask=="PAPER"):
            print('''YOU WON,
                  That's COOL 😎''')
        elif(x=="PAPER" and ask=="SCISSOR"):
            print('''YOU WON,
                  That's COOL 😀''')
        elif(x=="SCISSOR" and ask=="PAPER"):
            print('''YOU LOST,
                  Better Luck Next Time 🤕''')
        elif(x=="SCISSOR" and ask=="ROCK"):
            print('''YOU WON,
                  That's COOL 😎''')
        elif(x=="PAPER" and ask=="ROCK"):
            print('''YOU LOST,
                  Better Luck Next Time 🙃''')
    
    

#quiz:- guess the number
def quiz():
    print("In case you want to exit Guess The Number, Just don't enter any numbers for guessing")
    while True:
        
        inp=[int(x) for x in input("PLease enters the number from which you wanna start : ").split()]
        n=len(inp)
        if(n==0):
            break

        pc=random.randint(0,n)
        you=int(input("What's Your Guess : "))

        if(you in inp):
            print("The real answer is : ",pc)
            if(you==pc):
                print("You are on right path")
            elif(0<(you-pc)<5 or 0<(pc-you)<5):
                print("Close")
            elif((you-pc)<10 or (pc-you)<10):
                print("You are still away")
            else:
                print("Don't Give up, Keep Tring Away")
        else:
            print("ERROR!!! Kindly Choose any VALID NUMBER")
    print("Thanks for trying Guess the number, Have a GREAT DAY")
        
        
#binary search
def binarySearch(arr, x):
    n=len(arr)
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end)//2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            end = mid - 1
        else:
            start = mid+1

#contact book
def conbook():
    
    names=[]
    number=[]
    n=int(input("Enter how many contacts you want to add right now : "))
    
    for i in range(n):
        name=input("Enter the name >> ")
        phone=input("Enter the phone number >> ")
        names.append(name)
        number.append(phone)
    
    ask1 = input("Do you want to see your current Contact List ? ")
    if(ask1=="yes"):
        for i in range(len(names)):
            print("Names : {} & Phone Number : {}".format(names[i],number[i]))
        
    ask2 = input("Do you want to update Contact List ? : ")
    if(ask2=="yes"):
        en=input("Enter the name for which you want to update : ")
        indi=names.index(en)
        am=input("Enter yes to rename : ")
        if(am=="yes"):
            new=input("Enter The New Name : ")
            names[indi]=new
        an=input("Enter yes to modify phone number : ")
        if(an=="yes"):
            new=input("Enter The New Number : ")
            number[indi]=new
        for i in range(len(names)):
            print("Names : {} & Phone Number : {}".format(names[i],number[i]))

    ask3=input("Do you want to delete any contact ? : ")
    if(ask3=="yes"):
        ak=input("Enter the name of contact which you want to delete : ")
        ind=names.index(ak)
        del names[ind]
        del number[ind]
        for i in range(len(names)):
            print("Names : {} & Phone Number : {}".format(names[i],number[i]))
            
            
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")            
print("|>-----------------------------------<|")
print("|>-----------------------------------<|")
print("|>-----------------------------------<|")
print("|>-----------UTILITY POCKET----------<|")
print("|>-----------------------------------<|")
print("|>-----------------------------------<|")
print("|>-----------------------------------<|")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print('''THE FOLLOWING TOOLS ARE CURRENTLY AVAILABLE IN TOOLBOX : 
1] STANDARD CALCULATOR
2] RANDOM PASSWORD GENERATOR
3] GAME(ROCK,PAPER & SCISSOR)
4] QUIZ(GUESS THE NUMBER)
5] BINARY SEARCH
6] CONTACTS BOOK
#Enter '0' to exit the program !!!''')

while True:

    asky=int(input("Select Tool you wanna go with : "))
    if(asky==1):
        calculator()
    elif(asky==2):
        rpg()
    elif(asky==3):
        rps() 
    elif(asky==5):
        while True:
            arr=[int(x) for x in input("Enter the Sorted Integer List : ").split()]
            if(len(arr)==0):
                break
            x = int(input("Element you wanna find out : "))
            print("The Element You asked is at Index : ")
            print(binarySearch(arr,x))
        print("Thanks For Using BINARY SEARCH TOOL, Live Your Life with Purpose !")    
        
    elif(asky==4):
        quiz()
    elif(asky==6):
        conbook()
    elif(asky==0):
        print("Thanks For using Utility Pocket, I hope you had a great time !!!")
        break
    else:
        print("Kindly Choose any of These Programs, More Tools Will Be added Soon")
