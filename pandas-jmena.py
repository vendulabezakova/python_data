import pandas
import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena/assets/jmena.csv")

jmena = pandas.read_csv("jmena.csv")

# nastavení indexu na jméno
jmena = jmena.set_index("jméno")

# informace o jméně Jiří
print(jmena.loc["Jiří"])

# informace o jménech Martin, Zuzana a Josef
print(jmena.loc[["Martin", "Zuzana", "Josef"]])

# info o nejčastějších jménech po Martina
print(jmena.loc[ : "Martin"] ["četnost"])

# průměrný věk osob mezi Martinem a Terezou
print(jmena["Martin" : "Tereza"] ["věk"].mean())

# průměrný věk a původ všech jmen od Libora
print(jmena.loc["Libor" : , ["věk", "původ"]])

# sloupce mezi věkem a původem
print(jmena.loc[ : , "věk":"původ"])

