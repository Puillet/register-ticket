print("Hello World")

codeStateTab = ["FR", "UK", "DE", "IT", "ES"]
tvaValueTab = [20, 15, 19, 7, 10]

for elements in codeStateTab:
    print(elements)

print ("--------------")
montantHT = input("Saississez un montant H.T. \n")
print ("--------------")
montantTVA = input("Saississez un montant de TVA \n")

montantTTC = int(montantHT) + int(montantTVA)
print ("--------------")
print("Le montant TTC est égale à", montantTTC)