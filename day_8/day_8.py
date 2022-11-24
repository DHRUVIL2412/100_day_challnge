# # import random
# # small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# # capital=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# # endfill= [ ]
# # lastran = ' '
# # wannasmall = int(input("enter small"))
# # wannacap = int(input("enter capital letter"))
# # for i in range(0,wannasmall):
# #    endfill.append(random.choice(small))
# # for j in range(0,wannacap):
# #     endfill.append(random.choice(capital))
     
# # for i in len(endfill)-1:
# #    lastran+=random.shuffle(wannacap)
# # print(endfill)
# # import math
# # coverage = 5
# # height = int(input("enter the hight of the wall"))
# # width = int(input('enter the ammout of the width'))

# # def calculateseface(wallheight,wallwidth):
# #    printcal = (wallheight * wallwidth)/coverage
# #    printcal = math.ceil(printcal)
# #    print(printcal)
# # calculateseface(height,width)


# # prime number checker 
# # def primechecker(number):
  
# #    for i in range(1,number):
# #       if number%i == 0:
         
# #          print(f"{i}this is not a prime number ")
# #       if True :
# #          print(f"{i}this is a prime number ")
# #       else :
# #          print(f"{i} is not a prime number")

# # primechecker(10)




# # small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# # capital=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# # holder = []
# # takeit = input('enter seetance').lower()
# # for i in range(0,len(takeit)):
# #    holder.append(small.index(takeit[i]))
   
# # for i in range(0,len(holder)):
# #    # if small.index(i)<len(small):
# #    #    print('yes it big ')
# #    # else:
# #    #    print("no it small ")
# #    if holder[i]+3 < len(holder):
# #       print(holder)



# # widthWall = int(input("enter width of the wall"))
# # heightWall = int(input("enter the height of the width"))

# # ammountOfPaint = widthWall * heightWall /5
# # print(ammountOfPaint)

# # print(math.ceil(ammountOfPaint))



# # takeit = int(input("enter the cheker"))
# # prime = True
# # for i in range(2,takeit):
# #    if takeit%i == 0:
# #      prime = False
   
# # if prime:
# #    print("you are prime nubmer ")
# # else :
# #    print('you are not a prime number')

# # studentMarks = {
# #    'dhruvil':72,
# #    'ashish':30,
# #    'keval':12,
# #    'prince':76,
# #    'zell':50,
# #    'nirmal':12
# # }
# # studentgrade = { }

# # for student in studentMarks:
# #    if studentMarks[student]>70 and studentMarks[student]<100:
# #       print('outstanding')
# #       studentgrade[student]='outstanding'   
# #    elif studentMarks[student]>60 and studentMarks[student]<70:
# #       print('exeed expectation')
# #       studentgrade[student]='exeed expectation' 
# #    elif studentMarks[student]>40 and studentMarks[student]<60:
# #       print('acceptable')
# #       studentgrade[student]='acceptable' 
# #    elif studentMarks[student]>0 and studentMarks[student]<40:
# #       print('fail')
# #       studentgrade[student]='fail' 
# # print(studentgrade)

# # travel_city  = {
# #   "ahemedabad":{"city_visited":["love garden ",'kakriyalake','river front'],"total_visited":12},
# #    "surat":{"visited":['dhodkiya lake','diamond factory','kojway'],"foodlike":["panipuri",'dahipuri','pasta'],"remaining":"lost the city"},
# #    "junagadh":["amimal kingdome",'lion safari',"school","swaminarayan tample"]
# # }
# # ([('ahemedabad', {'city_visited': ['love garden ', 'kakriyalake', 'river front'], 'total_visited': 12}), ('surat', {'visited': ['dhodkiya lake', 'diamond factory', 'kojway'], 'foodlike': ['panipuri', 'dahipuri', 'pasta'], 'remaining': 'lost the city'}), ('junagadh', ['amimal kingdome', 'lion safari', 'school', 'swaminarayan tample'])])
# # print(travel_city.keys())
# # print(travel_city.values())
# # print(travel_city.items())
# # for i in travel_city: 
# #    print(travel_city[i])

# # travelCity = { }
# # def country(city,visited,numbers_of_time):
# #    travelCity['city'] = city
# #    travelCity['visited'] = visited
# #    travelCity['numbers of time'] = numbers_of_time
# # country("ahemedabad",["ran ki vav "],1)
# # print(travelCity)

# # travel_city  =    {
# #   "ahemedabad":{"city_visited":["love garden ",'kakriyalake','river front'],"total_visited":12},
# #    "surat":{"visited":['dhodkiya lake','diamond factory','kojway'],"foodlike":["panipuri",'dahipuri','pasta'],"remaining":"lost the city"},
# #    "junagadh":["amimal kingdome",'lion safari',"school","swaminarayan tample"]
# # }
# # ([('ahemedabad', {'city_visited': ['love garden ', 'kakriyalake', 'river front'], 'total_visited': 12}), ('surat', {'visited': ['dhodkiya lake', 'diamond factory', 'kojway'], 'foodlike': ['panipuri', 'dahipuri', 'pasta'], 'remaining': 'lost the city'}), ('junagadh', ['amimal kingdome', 'lion safari', 'school', 'swaminarayan tample'])])


# # bid = {}
# # AreHere = False
# # def findWinner(bidding_record):
# #    heighest = 0
# #    winner = " "
# #    for bidder in bidding_record:
# #       if heighest < bidding_record[bidder]:
# #          heighest = bidding_record[bidder]
# #          winner = bidder
# #    print("the winner is ", winner)
# # while not AreHere:
# #    userName = input("enter the name of the bidder")
# #    biddingAmmount = int(input("eter the ammout which bider can buy a stuff"))
# #    prompt = input("tell yes if any bidder is avalible")
# #    bid[userName] = biddingAmmount
# #    if prompt == "no":
# #       AreHere = True
# # findWinner(bid)



# firstCome = True
# def takeFirstValue(take1,take2,symboll):
#    result = 0
#    if result != 0:
#       result = take1
#    if symboll == "/":
#       result = take1 / take2
#    if symboll == "*":
#       result = take1 * take2
#    if symboll == "+":
#       result = take1 + take2
#    if symboll == "-":
#       result = take1 - take2
#    print(result)
#    return result
# for i in range(0,5):
#    if firstCome == True:
#       firstVal = int(input("enter the value of 1 st"))
#       firstCome = False
#    symbo = input("enter symboll of ")
#    secondVal = int(input('enter the second value'))
#    takeFirstValue(firstVal,secondVal,symbo)

# def leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("the year is leap year ")
                
#             else:
#                 print('this is not a leap year ')
                
#         else:
#             print("this is lepa year ")
            
#     else:
#         print("this is not a leap year ")

# def days_of_month(days,months):
#     month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if leap_year(months) and days==2:
#        return 29
#     return month_day[(days-1)]

# day = int(input('enter the the day '))
# month = int(input("enter the month"))

# print(days_of_month(day,month))

# def add(number,number2):
#     return number + number2
# def substact(number,number2):
#     return number - number2
# def multiply(number,number2):
#     return number * number2
# def dived(number,number2):
#     return number / number2
# operatorList = {
#     "+" : add,
#     "-" : substact,
#     "*" : multiply,
#     '/' : dived
#     }
# stopLoop = "y"

# firstNum = int(input("please enter the first value "))
# while stopLoop=="y":
#     for i in operatorList:
#         print(i)
#     operator = input("pick an operation from the line above ")
#     secondNum = int(input("please enter the second value "))
#     calculationfunc = operatorList[operator]
#     result = calculationfunc(firstNum , secondNum)
#     print(f"{firstNum}{operator}{secondNum}={result}")
#     secondSymboll = input("enter the symboll")
#     thirdNum  = int(input("enter thirdNum"))
#     nextResult = calculationfunc(result,thirdNum)
#     print(nextResult)
#     if input("are you continue to tunning") != "y":
#         stopLoop = False


# def add(firstVal,secondVal):
#     return firstVal+secondVal

# def  substraction(firstVal,secondVal):
#     return firstVal-secondVal

# def multipication(firstVal,secondVal):
#     return firstVal*secondVal

# def dividsion(firstVal,secondVal):
#     return firstVal/secondVal

# oparatorList = {
#     '+' : add,
#     '-' : substraction,
#     '*' : multipication,
#     '/' : dividsion
# }
# def newCalculation():
#     keepContinue = True
#     firstValue = int(input("enter the first value"))
#     while keepContinue:
#         symbol = input("plese enter the symoll")
#         secondValue = int(input("enter the second value "))
#         FetchedArray = oparatorList[symbol]
#         result  = FetchedArray(firstValue,secondValue)
#         print(f"{firstValue}{symbol}{secondValue}={result}")
#         if input(f"are you continue to work {result}")== "y":
#             firstValue = result 
#         else :
#             keepContinue = False
#         if input("are you going to new calculation ") =="y":
#             newCalculation()

# newCalculation()

def addtion(num1, num2):
    return num1+num2
def substraction(num1,num2):
    return num1-num2
def multipication(num1 , num2):
    return num1*num2
def devidsion(num1,num2):
    return num1/num2

symbollList = {
    '+':addtion,
    '-':substraction,
    '*':multipication,
    '/':devidsion
}

continueLooping = True
firstNumber = int(input("enter the first number"))
while continueLooping :
    for i in symbollList:
        print(i)
    symbol =input("plese enter the symboll")
    secondNumber = int(input("enter the second number "))
    fetchFromList = symbollList[symbol]
    resultAssumed = fetchFromList(firstNumber,secondNumber)
    print(f"{firstNumber} {symbol}={resultAssumed}") 
    
