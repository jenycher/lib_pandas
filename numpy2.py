#Обработка выбросов
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'value':[1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}

df = pd.DataFrame(data)

#5. Создадим график, который поможет визуализировать данные из датафрейма. Для этого мы будем использовать библиотеку Matplotlib:

df['value'].hist()
plt.show()