import pandas as pd

df = pd.read_csv('animal.csv')
#print(df)

#NaN заменяем на 0 , использовать команду fillna
#df.fillna(0, inplace=True)
#print(df)

#NaN удаляем
#df.dropna(inplace=True)
#print(df)

# Группировка данных
#group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
#print(group)

# процедуры для изменения исходной таблицы
data = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
    }

df = pd.DataFrame(data)
df.to_csv('outpu.csv', index=False)

