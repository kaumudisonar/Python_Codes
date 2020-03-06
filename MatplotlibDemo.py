import pandas as pd
import matplotlib.pyplot as plt

filename='Marvellous.xlsx'
data=pd.read_excel(filename)
# # print(data)
# # print(data.head())
# print(data.tail())
print(data.shape)

sort=data.sort_values(['Name'],ascending=True)
print(sort)

data['Age'].plot(kind="hist")
plt.show()

data['Age'].plot(kind="barh")
plt.show()