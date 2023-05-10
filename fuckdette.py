# Funksjon for å legge sammen to tall
def addisjon(a, b):
    return a + b

# Funksjon for å trekke fra to tall
def subtraksjon(a, b):
    return a - b

# Funksjon for å multiplisere to tall
def multiplikasjon(a, b):
    return a * b

# Funksjon for å dividere to tall
def divisjon(a, b):
    return a / b

# Hovedprogrammet
print("Velkommen til den enkle kalkulatoren!")

# Les inn tallene fra brukeren
nummer1 = float(input("Skriv inn det første tallet: "))
nummer2 = float(input("Skriv inn det andre tallet: "))

# Utfør de fire grunnleggende operasjonene
summen = addisjon(nummer1, nummer2)
differansen = subtraksjon(nummer1, nummer2)
produktet = multiplikasjon(nummer1, nummer2)
kvotienten = divisjon(nummer1, nummer2)

# Skriv ut resultatene
print("Summen av tallene er:", summen)
print("Differansen mellom tallene er:", differansen)
print("Produktet av tallene er:", produktet)
print("Kvotienten mellom tallene er:", kvotienten)
