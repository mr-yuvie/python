import random
import time

Letters=['E','T','I','A','N','M','S','U','R','W','D','K','G','O','H','V','F','L','P','J','B','X','C','Y','Z','Q']

#FINISH THE MORSE CODE LETTERS.
Letters_Morse=[".","-","..",".-","-.","--","...",]

Numbers=[0,5,1,2,3,4,6,7,8,9]

Symbols=['+','=','/']

chance1=['yes','no']
chance2=['yes','no','maybe']

test=''

#EASY
def easy():
    length=15
    while length>0:
        global test
        if random.choice(chance2)=='maybe':
            if random.choice(chance1)=='yes':
                test=test+str(random.choice(Numbers))
                length-=1
        else:
            test=test+str(random.choice(Letters))
            length-=1
    print(test)
    check()
#CHECKING
def check():
    per=0
    if choice=='EASY':
        length=15
    answer=input("Enter Answer:")
    for i in range(len(answer)):
        if answer[i]==test[i]:
            per+=1
    Accuracy=(per/length)*100
    print("Your Accuracy:",Accuracy,"%")

while True:
    choice=input("Enter Difficulty:")
    if choice=='EASY':
        easy()
    else:
        break

""" FOR SYMBOLS
elif random.choice(chance2)=='maybe':
if random.choice(chance2)=='maybe':
if random.choice(chance1)=='yes':
test=test+str(random.choice(Symbols))
length-=1"""
#print(random.choices(Letters,k=6))#print(random.choices(Letters,k=6))