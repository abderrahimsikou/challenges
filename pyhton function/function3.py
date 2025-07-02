print('============factorial============')
def factorial():
    number = int(input('Enter Number To factorial:'))
    x = 1
    for i in range(1, number + 1):
        x *= i
    print(x)
factorial()

#==========================================
print('============multiplication============')
def multiplication():
    number = int(input('Enter Number To multiplicated:'))
    for i in range(1, 11):
        print(f'{number} * {i} = {number * i}')
multiplication()

#===========================================
print('============carre_parfait============')
import math

def carre_parfait():
    number = int(input('Enter Number:'))
    if number%math.sqrt(number) == 0:
        print('carré parfait')
    else:
        print('carré Non parfait')
carre_parfait()
    
#===========================================
print('==========chaine============')
def chaine():
    name = input('Enter chaine:')
    for x in name:
        print(x)
chaine()

#===========================================
print('==========phrace============')
def phrace():
    phrace = input('Enter sentence:')
    split = phrace.split()
    long = max(split, key=len)
    print(f'longest word: {long}')
phrace()

#===========================================
print('==========ch============')  

def chaine_de_caractères():
    ch = input('Enter sentence:')
    x = {}
    for caractere in ch.lower():
        if caractere != ' ':
            x[caractere] = x.get(caractere, 0) + 1
    for caractere, y in x.items():
        print(caractere, y)
chaine_de_caractères()