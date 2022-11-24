
# import random
# rndm = random.randint(0,2)
#
# componentOfGame = ['stone','paper','scissor']
#
# computerInput = componentOfGame[rndm]
# uInput = int(input("enter the stone of 0 paper for 1 scissior 2"))
# userInput = componentOfGame[uInput]
# if(computerInput==userInput):
#     print("the match is draw ")
#
# if(computerInput =="stone" and userInput =="paper"):
#     print("winn user")
# if(computerInput =="paper" and userInput =="scissor"):
#     print("winn user")
# if(computerInput =="stone" and userInput =="scissor"):
#     print("winn comute")
# if(computerInput =="scissor" and userInput =="paper"):
#     print("winn comute")
# if(computerInput =="scissor" and userInput =="ston"):
#     print("winn user")
# if(computerInput =="paper" and userInput =="stone"):
#     print("winn comute")
#
# print(computerInput)
# print(userInput)
# import random
# us = random.randint(0,1)
# virtualCoinTossPosibility = ['head','tail']
# print(virtualCoinTossPosibility[us])

# takeit = input("give the name sapreted by the coma")
# busineess = takeit.split(",")
# print(busineess)
# print(busineess[0])

# import random
# getthings = input('enter the value of coma seprated')
# alreadySplits = getthings.split(',')
# print("buy mill today is "+alreadySplits[random.randint(0,(len(alreadySplits)-1))])

# import random
# getthings = input('enter the value of coma seprated')
# alreadySplits = getthings.split(',')
# print(random.choice(alreadySplits))

# import random
# num = [1,2,3,4,5,6,7,8,9,0]
# capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',"T",'U','V','W','X','Y','Z']
# small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# symbolls = ['!','@','#','$','%',"^",'&','*','(',")",'_','-',"+","=","{","}",'[',']','|',"<",">",',','.',"?","/","~","`"]

# # requriedlan =(input("enter your password langth"))
# usercap = int(input("enter about of capital requried"))
# usersmall =int (input("enter about of small requried"))
# usersym =int (input("enter about of symboll requried"))
# usernum =int (input("enter ammount of number is have you"))

# password =[]
# mainpass =""
# for p in range(1,usercap+1):
#     password += str(random.choice(capital))
# for p in range(1,usersmall+1):
#     password += str(random.choice(small))
# for p in range(1,usernum+1):
#     password += str(random.choice(num))
# for p in range(1,usersym+1):
#     password += str(random.choice(symbolls))

# random.shuffle(password)
# for i in range(0,len(password)):
#     mainpass += password[i]

# print(mainpass)
# sumti =0
# stoplimit = input("stoplimit enter").split()
# for i in range(0,len(stoplimit)):
#     stoplimit[i] = int(stoplimit[i])
# print(type(stoplimit[2]))
# avgn = len(stoplimit)
# for k in stoplimit:
#     sumti = sumti+k
# print(sumti/avgn)

# sumti =0
# stoplimit = input("stoplimit enter").split()
# for i in range(0,len(stoplimit)):
#     stoplimit[i] = int(stoplimit[i])
# print(type(stoplimit[2]))
# avgn = len(stoplimit)
# for k in stoplimit:
#     sumti = sumti+k
# print(sumti/avgn)

# highscore = [12,23,4,43,45,56,75,23,45,94,66]
# score = 0
# secondhi = 0
# third =0
# for i in range(0,len(highscore)-1):
#     if(highscore[i]>highscore[i+1]):
#         score=highscore[i]
# for i in range(0,len(highscore)-1):
#     if(highscore[i]>highscore[i+1] and highscore[i]<score):
#         secondhi=highscore[i]
# for i in range(0,len(highscore)-1):
#     if(highscore[i]<score and highscore[i]<secondhi and highscore[i]<highscore[i+1]):
#         third=highscore[i]

# print(score)
# print(secondhi)
# print(third)

# scores = [12,23,45,64,34,54,34,5,67,89,34]
# high_score = 0
# second_high = 0
# third_high =0
# for score in scores:
#         if score > high_score:
#             high_score = score
# for score in scores:
#         if score>second_high and score!=high_score:
#             second_high = score
# for score in scores:
#         if score>third_high and score!=high_score and score!=second_high:
#             third_high = score
# print(high_score)
# print(second_high)
# print(third_high )

# for i in range(1,100):
#     if(i%3==0 and i%5==0):
#         print("fizzbuzz")
#     elif(i%5==0):
#         print("buzz")
#     elif(i%3==0 ):
#         print("fizz")
#     else:
#         print(i)
loweLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
endResult = ""
word=input("enter your name").lower()
# entersteps = int(input('enter steps'))
bunch = " "
for i in range(0,len(word)):
    if True:
       bunch+=str(loweLetter.index(word[i]))
print(bunch)
