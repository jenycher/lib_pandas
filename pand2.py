import pandas as pd

df = pd.read_csv('hh.csv')
df['Test'] = [new for new in range(29)] #добавляем столбец
#Цикл for здесь будет перебирать список, который создаётся с помощью команды range из 29 чисел (от 0 до 28) и будет подставлять их в список, где они будут сохраняться.
print(df)

df.drop('Test', axis=1, inplace=True) #удаление
print(df)

df.drop(28, axis=0, inplace=True) # удаление строки 28
print(df)