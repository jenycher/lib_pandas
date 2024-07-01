#Обработка выбросов
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'value':[1, 2,2, 3, 3, 3, 4, 4, 4, 4,5, 6, 7, 8, 9, 10, 55]}

df = pd.DataFrame(data)

#5. Создадим график, который поможет визуализировать данные из датафрейма. Для этого мы будем использовать библиотеку Matplotlib:

#df['value'].hist() # вывод гистограммы
df.boxplot(column='value')
plt.show()

# на гистограмме мы видим отдельный выбор - цифра 55 выбивается

# в дальнейшем выбор чаще удаляют данные

#print(df.describe())

Q1 = df['value'].quantile(0.25) #квартили
Q3 = df['value'].quantile(0.75) #квартили
IQR =Q3 - Q1 #межквартальный размах

downside = Q1 - 1.5 * IQR
upside  = Q3 + 1.5 * IQR

df_new =df[(df['value'] >= downside) & (df['value'] <= upside)]
df_new.boxplot(column='value')
plt.show()

