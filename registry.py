print("Hello World")

codeStateTab = ["FR", "UK", "DE", "IT", "ES"]
tvaValueTab = ["20", "15", "19", "07", "10"]
i = 0 

print("-----------")
print("|Pays| TVA |")
print("-----------")
for elements in codeStateTab:
    print("|", elements, "|", tvaValueTab[i], "|")
    print ("-----------")
    i += 1

montantHT = input("Saisissez un montant H.T. \n")
print("--------------")
codePays = input("Saisissez le code Pays \n")

paysValue = codeStateTab.index(codePays)
montantTVA = tvaValueTab[paysValue]


montantTVA = float(montantTVA) / 100
montantTVA = float(montantHT) * float(montantTVA)
montantTTC = float(montantHT) + float(montantTVA)

print("--------------")
print("Le montant TTC est égal à", montantTTC)