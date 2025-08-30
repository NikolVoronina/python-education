import random


tall = input("Skriv inn et tall mellom 1 og 100: ")
random_tall = random.randint(1, 100)
if int (tall) is random_tall:
    print("Gratulerer! Du gjettet riktig!")     
if int (tall) > random_tall:
    print("Tallet er lavere enn det du gjettet.")
elif int (tall) < random_tall:
    print("Tallet er høyere enn det du gjettet.")

while int (tall) is not random_tall:
    tall = input("Skriv inn et tall mellom 1 og 100: ")
    if int (tall) is random_tall:
        print("Gratulerer! Du gjettet riktig!")     
    if int (tall) > random_tall:
        print("Tallet er lavere enn det du gjettet.")
    if int (tall) < random_tall:
        print("Tallet er høyere enn det du gjettet.")