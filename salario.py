import pandas as pd
import matplotlib.pyplot as plt

salarios = pd.read_csv("C:\\Users\\f0fp1107\\Downloads\\salarionominalnecessario.csv", sep=",", encoding="latin_1")
print(salarios.head())

salarios['perc'] = salarios['Salário mínimo nominal']/salarios['Salário mínimo necessário']
print(salarios.head())

salarios = salarios.iloc[::-1]
salarios = salarios[len(salarios)-12:]
datas = pd.date_range(start='2022-09',end='2023-08',periods=12)
datas = datas.strftime('%m/%Y')

plt.plot(datas,salarios['perc'])
plt.xlabel("Período")
plt.ylabel("Percentual do necessário possuído pelo mínimo")
plt.show()