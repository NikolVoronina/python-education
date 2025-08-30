tilfeldigeTall= [3, 6, 1, 9, 4, 7, 5]
print(tilfeldigeTall)

likFem = tilfeldigeTall.count(5)
print ('Hvor mange tall som er lik 5 : ', likFem)

storreEnFem = 0
for tall in tilfeldigeTall:
    if tall > 5 :
        storreEnFem += 1

print ('tallene som er større enn 5 : ' , storreEnFem)