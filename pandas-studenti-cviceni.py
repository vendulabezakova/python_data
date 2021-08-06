import pandas
import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/excs/studenti/assets/jmena.csv")
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/excs/studenti/assets/studenti1.csv")
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/excs/studenti/assets/studenti2.csv")

studenti1 = pandas.read_csv("studenti.csv")
studenti2 = pandas.read_csv("studenti2.csv")

#print(jmena.head)
#print(studenti1.head)
#print(studenti2.head)

# spojení datových setů
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)

# kolik nestuduje a kolik je dálkových
print(len(studenti[studenti["ročník"].isna()]), "nestuduje")
print(sum(studenti["kruh"].isna()), "je dálkových")

# kolik prezenčních studentů je v oboru
print(studenti.groupby("obor").count())

# průměrný prospěch
print(studenti.groupby("obor")["prospěch"].mean())

# načíst dataset s křestními jmény + spojit s tabulkou studentů
jmena = pandas.read_csv("jmena.csv")
print(pandas.merge(jmena, studenti, on=["jméno"]))

# diverzita na IT fakultě :-)
print(jmena.groupby("pohlaví").count())

