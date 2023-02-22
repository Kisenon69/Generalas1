import random 

#0 
print("Osztálzatok generálása.")

#1
db = int(input("Kérem az osztályzatok számát"))

osztalyzatok = []
#mivel ismerjük a drbok számát- ezért a generálást előre meghatározott ciklusba végezzük.
for i in range(db):
    oszt = random.randint(1,5)
    osztalyzatok.append(oszt)

#2-3
print(osztalyzatok)