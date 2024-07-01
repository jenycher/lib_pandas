#Работа с категориАльными данными в Pandas
#КатегориАльные данные — это данные, которые могут принимать одно из ограниченного набора значений.
import pandas as pd
data = {
         'name': ['Alice','Bob', 'Charlie', 'David', 'Eve'],
         'gender': ['female', 'male', 'male', 'male', 'female'],
         'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
    }

df = pd.DataFrame(data)
#Команда astype преобразует гендер и департамент в категориальный тип, что позволяет работать с этими данными как с категориями.
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')

print(df['gender'].cat.categories) #вывели все категории
print(df['department'].cat.categories)
print(df['gender'].cat.codes) # числовые коды категорий

#добавить новую категорию — например, новый департамент, финансовый отдел.
df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)

# Видим, что новая категория не добавилась.Это произошло потому, что
# мы не сохранили внесённые изменения в изначальном датафрейме.Для этого
#исправим предыдущую строку:

df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)

#можем удалить категорию. Для этого вместо команды add нужно прописать remove:
df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)

print(df) # появятся NaN где удаляли данные

