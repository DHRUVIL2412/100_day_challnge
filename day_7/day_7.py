# import random
# stay =""
# wordList = ["mouse","bet","lock"]
# cmpGuess= random.choice(wordList)
# wording = cmpGuess
# lenggess= len(cmpGuess)
# print(lenggess)
# print(cmpGuess)
# for i in range(0,lenggess):
#     stay+="_"
#     print(stay)
#     userGuess = input("Guess the latter")
#     for i in range(0,5):
#         if(wording[i]==userGuess):
#             stay.replace("_",wording[i])
#             print(stay)       
# import random
# wordList = ["advertise","mouse","rabbit"]
# pickOne = random.choice(wordList)
# print(pickOne)
# stay = [ ]
# for i in range(0,len(pickOne)):   
#     guess = input("enter letter").lower()
#     for letter in  pickOne:
#         if letter == guess:
#             stay.append(letter)
#             print(letter.replace(letter,guess),end=' ')   
            
#         else :
#             stay.append(letter)
#             print(letter.replace(letter,"'_'"),end =" ")
# print(stay)


# import random 
# wordList = ["camle","contenent",'phycology']
# getRandom = random.choice(wordList)
# lenthof = len(getRandom)
# display = []
# for _ in range(lenthof):
#     display +='_' 
# print(display)
# while display!='_':
#     userInput = input("enter the guessed word ")
#     # for position in range(lenthof):
#     for position in range(lenthof):
#         letter=getRandom[position]
#         if(letter==userInput):
#             display[position]=letter
#     print(display)

# Letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# loweLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
# endResult = []
# word=input("enter your name").lower()
# # entersteps = int(input('enter steps'))
# bunch = []
# for i in range(0,len(word)):
#     if True:
#        bunch.append(str(loweLetter.index(word[i])))
# print(bunch)

# for i in bunch:
#     cameout=(int(i)+3)
#     if cameout < len(loweLetter):
#         endResult.append(int(i)+3)
#     else :        
#         endResult.append((cameout-28+3))
# print(endResult)

# for lo in endResult:
#     print(loweLetter[lo],end="")

result = 0
firstCome = True
def takeFirstValue(take1,take2,symboll):
   if result != 0:
      result = take1
   if symboll == "/":
      result = take1 / take2
   if symboll == "*":
      result = take1 * take2
   if symboll == "+":
      result = take1 + take2
   if symboll == "-":
      result = take1 + take2
   print(result)

if firstCome == True:
   firstVal = int(input("enter the value of 1 st"))
   firstCome = False
symbo = input("enter symboll of ")
secondVal = int(input('enter the second value'))

takeFirstValue(firstVal,secondVal,symbo)