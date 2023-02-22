import random

#0
print("Egy osztály tanulóinak generálása.")

vNevek=["Ádám", "Balogh", "Lakatos", "Tóth", "Rézműves", "Váradi"]
ferfiKnevek=["András", "Béla", "Géza", "József", "István"]
noiKnevek=["Anita", "Ildiko", "Erika", "Mariann"]

db=int(input("Kérem a tanulók számát."))
tanulok = []
for i in range(db):
    #tanulo neve
    neme=random.randint(1,2)
    if neme.lower()=="férfi":
        teljesNev = random.choice(vNevek)+' '+random.choice(ferfiKnevek)
        neme="férfi"
    elif neme.lower()=="nő":
        teljesNev = random.choice(vNevek)+' '+random.choice(noiKnevek)
        neme="nő"
    #tanulo szuletesi ideje
    ev=random.randint(2000, 2005)
    honap=random.randint(1, 12)
    nap=random.randint(1, 28)
    datum= f"{ev}.{honap:0>2d}.{nap:0>2d}"
    #magassag
    magassag=random.randint(155,190)

    #tanulo összeállítása
    tanulo = (teljesNev, datum, neme, magassag)

    #felvétel a tanulóhoz
    tanulok.append(tanulo)


#2-3
for item in tanulok:
    print(item)
