
# import random
# print(" you are palying a guess game")
# randomeNumber = random.randint(0,100)
# if input("enter the dificuty leval is 'easy' or 'hard' ") == "easy":
#     for i in range(0,10):
#         print(f"you have only {10-i} choice to accomplce that task")
#         guessedWord =int(input("enter the number you guessed"))
#         if guessedWord<randomeNumber:
#             print("you are guess two small number")
#         elif guessedWord>randomeNumber:
#             print("you are guess two big number")
#         elif guessedWord==randomeNumber:
#             print("you are perfect guess and win")
#             i=4
# else :
#         for i in range(0,5):
#             print(f"you have only {5-i} choice to accomplce that task")
#             guessedWord =int(input("enter the number you guessed"))
#             if guessedWord<randomeNumber:
#                 print("you are guess two small number")
#             elif guessedWord>randomeNumber:
#                 print("you are guess two big number")
#             elif guessedWord==randomeNumber:
#                 print("you are perfect guess and win")
# #                 i=4
# import random
# easy_leval = 10
# hard_leval = 5
# randomeThink = random.randint(0,100)
# print("think number between 0 to 100")

# def checkLeval():
#     leval = input("enter the leval you wanna 'easy' or 'hard'")
#     if leval == "easy":
#         return easy_leval
#     else :
#         return hard_leval
# turns = checkLeval()
# print(randomeThink)

# def checkAnswer(guess,answer,turns):
#     if guess > answer:
#         print("your guessed number is too big plese reduce it")
#         return  turns-1
#     elif guess <answer:
#         print("your answer is to low plase increse it ")
#         return  turns-1
#     else:
#         print(f"you are winn the game and your guessed number is {answer} ")


# def userGuess():   
#     userInput = 0
#     while userInput != randomeThink:
#         userInput= int(input("enter your guessed number and run"))
#         print(turns)
#         turs = checkAnswer(userInput,randomeThink,turns)
#         if turs == 0 :
#             print('you lose the game')
#             return 

# # userGuess()
# import random 

# autoGuess = random.randint(0,100)
# print(autoGuess)

# easy_leval = 10
# hard_leval = 5

# def hardOrEasy():
#     if input("select the game 'easy' or 'hard' ") == 'easy':
#         return easy_leval
#     else :
#         return hard_leval
# numberofItration = hardOrEasy()

# def sudggetion(takeit,autoGuess,index):  
#     if takeit > autoGuess:
#         print("your value is too big plese reduse it")
#         return index-1
#     elif takeit < autoGuess:
#         print("your value is too low plese increse it")
#         return index-1
#     else:
#         print(f"your are win the game and your sudgetion is {autoGuess}")

# def userinput():
#     takeinput = 0   
#     while autoGuess!=takeinput:
#         takeinput = int(input("please guess thr number"))
#         sudggetion(takeinput,autoGuess,numberofItration)
#         print(numberofItration)
#         if numberofItration == 0:
#             return
# userinput()

# def myrun():
#     for i in range(1,10):
#         def muflish():
#             print("make over")
#         if i%2==0:
#             print("you arre got this"+str(i))   
#         if i==3:
#             muflish()
# # myrun()
# from random import randint
# lis = ['1','2','3','4','5','6']
# print(lis[randint(0,5)])

# page = 0
# page_per_word = 0
# page = int(input("enter the page number "))
# page_per_word = int(input('enter the page per book'))
# total = page*page_per_word
# print(total)


# def muted(a_list):
#     b_list=[]
#     for i in a_list:
#         new_item = i*2
#         b_list.append(new_item)
#     print(b_list)

# newarray = [10,20,30,40,50]
# muted(newarray)
    
# userinput = int(input("entr the year you check"))
# if userinput%4 ==0:
#     if userinput % 100 == 0:        
#         if userinput % 400 == 0: 
#             print("this is a leap year")
#         else:
#             print("this is not a leap year")
#     else :
#         print("this is leap year")
# else :
#     print("this is not leap year")


# from game_data import data
# import random

# def format_data(account):
#     account_name = account['name']
#     account_follower_count = account['follower_count']
#     account_description = account['description']
#     account_country = account['country']
#     return (f"is {account_name} description about is {account_description} and country is {account_country}")

# def checkUserIsRight(guess,accountA,accountB):
#     if accountA['follower_count']>accountB['follower_count']:
#         return guess =='a'
#     else :
#         return guess=='b'
# score = 0
# endGame = True
# account_b = random.choice(data)
# while endGame:
#     account_a = account_b
#     account_b = random.choice(data)

#     if account_a == account_b:
#         account_b = random.choice(data)

#     print(format_data(account_a))
#     print(format_data(account_b))
#     guess = input("you like enter the ammount of more followers 'a' or 'b' ").lower()
#     is_checked = checkUserIsRight(guess,account_a,account_b)
#     if is_checked:
#         score=score+1
#         print(f"ya u are right {score}")
#     else :
#         endGame = False
#         print("off u are flase {score}")


#
# from game_data import data
# import random
# gameisRunning = True
# account_b = random.choice(data)
# def aboutAccount(account):
#     account_name = account['name']
#     account_description = account['description']
#     account_country = account['country']
#     return (f"{account_name}and about {account_description}and country is {account_country}")
# def checkStatus(guess, accountA, accountB):
#     if accountA['follower_count'] > accountB['follower_count']:
#         return guess=='a'
#     else :
#         return guess=='b'
# score = 0
# while gameisRunning:
#     account_a = account_b
#     account_b = random.choice(data)
#
#     if account_b == account_a:
#         account_b = random.choice(data)
#     print(aboutAccount(account_a))
#     print(aboutAccount(account_b))
#     guess = input("enter your choice account a is biger than account b")
#
#     isTrue = checkStatus(guess,account_a,account_b)
#
#     if isTrue:
#         score = score +1
#         print(f"you are choice is right{score}")
#     else:
#         gameisRunning = False
#         score = 0
#         print(f"you are choice is false{score}")

Menu = {
    'latte':{
        'ingredients':{
            'water':200,
            'milk':150,
            'coffee':24
        },
        'cost':2.5
    },
    'espresso':{
        'ingredients':{
            'water':50,
            'milk':0,
            'coffee':18
        },
        'cost':1.5
    },
    'cappuccino':{
        'ingredients':{
            'water':250,
            'milk':100,
            'coffee':24,
        },
        'cost':3.0
    }

}
resource = {
    'water':300,
    'milk':200,
    'coffee':100
}
profit = 0
machineStatus = True

def checkResources(coffeeType):
    'return if we have enough resourse'
    for item in coffeeType:
        if coffeeType[item] > resource[item]:
            print("sorry the fullfield resounce is not avaible")
            return False
        return True

def processCoin():
    'return a coin value'
    print("plese insert coins. ")
    total = int(input("how many quarters?: "))*0.25
    total += int(input('how many dims?:'))*0.10
    total += int(input('how many nikles ?:'))*0.05
    total +=int(input('how many panny'))*0.01
    return total

def isPaymentSuccessfull(moneyRecived , coffeeCost):
    if moneyRecived>coffeeCost:
        global profit
        change = round(moneyRecived-coffeeCost,2)
        profit += coffeeCost
        print(f'take your change return back into your pocket{change}')
        return True
    else:
        print('you have not enogh money plese give more case')
        return False

def makeCoffee(drinkName , order_ingredients):
    for item in order_ingredients:
        if resource[item] > order_ingredients[item]:
            resource[item] -= order_ingredients[item]   
        else:
            print("u have not enogh resourse")
    print(f"here's your coffee ☕️ {drinkName}")
    

while machineStatus:
    user_need = input("what whould you like to have ? (latte/cappuccino/espresso)").lower()
    if user_need == 'turn off':
        machineStatus = False
    elif user_need == 'report':
        print(f'water {resource["water"]}ml')
        print(f'milk {resource["milk"]}ml')
        print(f'coffee {resource["coffee"]}gm')
        print(f'profit is ${profit}')
    else:
        drink = Menu[user_need]
        print(drink)
        checkResources(drink['ingredients'])
        payment = processCoin()
        if isPaymentSuccessfull(payment,drink['cost']):
            makeCoffee(user_need,drink['ingredients'])





















































































































































