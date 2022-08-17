#diceBot v0.2.py
#?---Imports---
from random import randint
from discord import Embed, Color

async def diceFunction(message):
    #?---User Input---
    diceInput = message.content 
    diceInput = diceInput.partition("!dice") [2]
    diceInput = diceInput.upper()

    #?---Variables---
    diceLst = []
    diceDict = {}
    operatorLst = ["+", "-", "/", "*"]
    operator = ""
    operatorNum = ""
    operatorAns = ""
    emb = Embed()

    #?---Main Loop---
    for die in diceInput.split(":"):
        match = next((x for x in operatorLst if x in die), False)
        if match:
            operator = match
            operatorNum = int(die.partition(operator)[2])
        else:
            diceLst.append(die)

    for item in diceLst:
        diceAmount = int(item.partition("D") [0])
        diceSides = int(item.partition("D") [2])
        diceType = "D" + str(diceSides)

        diceDict[diceType] = [diceAmount, diceSides]

    #print(f"Throw Operator: {operator} {operatorNum}")
    #print("Dice Dictionary:")
    for item in diceDict:
        diceLst.append(item)

    throwTotal = 0
    for key in diceDict: 
        #print(f"Throwing: {key}")
        diceAmount = diceDict[key][0]
        diceSides = diceDict[key][1]
        #print(f"Throw Amount: {diceAmount}")
        #print(f"Dice Sides: {diceSides}")

        throwLst = []
        for i in range(diceAmount):
            throwVal = randint(1, diceSides)
            #print(f"Throw value: {throwVal}\n")
            throwTotal += throwVal
            throwVal = str(throwVal)
            throwLst.append(throwVal)
            #emb.add_field(name = f"{key} Roll {i + 1}", value = throwVal, inline=True)
        throwLstStr = ", ".join(throwLst)
        emb.add_field(name = f"{key}", value = f"**Roll Results:** {throwLstStr}", inline=True)

    if operator == "+":
        operatorAns = throwTotal + operatorNum
    elif operator == "-":
        operatorAns = throwTotal - operatorNum
    elif operator == "/":
        operatorAns = throwTotal / operatorNum
    elif operator == "*":
        operatorAns = throwTotal * operatorNum
    #color = Color.orange(), 
    #?---Final Results---
    diceInput = diceInput.replace(':', ' : ')
    emb.color = Color.orange()
    emb.description = f"**Total Throw Value: {throwTotal}\nThrow Operator: {throwTotal} {operator} {operatorNum}\nFinal Throw Value: {operatorAns}**"
    #emb = Embed(description= f"Total Throw Value: {throwTotal}\nThrow Operator: {throwTotal} {operator} {operatorNum}\nFinal Throw Value: {operatorAns}") 
    emb.set_author(name = message.author.display_name + f"Rolled: {diceInput}", icon_url = message.author.avatar_url)
    await message.channel.send(embed=emb)

    







