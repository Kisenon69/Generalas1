import random

#0
print("Egy emberi név generálása.")

vNevek=["Ádám", "Balogh", "Lakatos", "Tóth", "Rézműves", "Váradi"]
ferfiKnevek=["András", "Béla", "Géza", "József", "István"]
noiKnevek=["Anita", "Ildiko", "Erika", "Mariann"]

#1
neme=input("Kérem az ember nemét (férfi\|/nő) : ")

if neme.lower()=="férfi":
    teljesNev = random.choice(vNevek)+' '+random.choice(ferfiKnevek)
elif neme.lower()=="nő":
    teljesNev = random.choice(vNevek)+' '+random.choice(noiKnevek)
else:
    print("HIBA: rossz nemet adott meg")
    exit()

#2-3

print(teljesNev)

