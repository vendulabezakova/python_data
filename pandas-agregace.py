import pandas
import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u202.csv")
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u203.csv")
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u302.csv")
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/studenti.csv")
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/predsedajici.csv")

u202 = pandas.read_csv("u202.csv")
u203 = pandas.read_csv("u203.csv")
u302 = pandas.read_csv("u302.csv")
predsedajici = pandas.read_csv("predsedajici.csv")

maturita = pandas.concat([u202, u203, u302], ignore_index=True)
studenti = pandas.read_csv("studenti.csv")

# spojení tabulek
#print(pandas.merge(maturita, studenti))
# uložení tabulek
maturita = pandas.merge(maturita, studenti)
#print(predsedajici.head())

maturitaPredseda = pandas.merge(maturita, predsedajici, on=["den"])
maturitaPredseda.rename(columns={"jmeno_x": "jmeno_studenta", "jmeno_y": "jmeno_predsedy"})
#print(maturitaPredseda.info)

print(maturita.groupby("predmet") ["znamka"].mean())