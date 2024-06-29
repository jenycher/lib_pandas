import pandas as pd

# Загрузка данных из CSV-файла в DataFrame
file_path = 'coffee_survey.csv'
df = pd.read_csv(file_path)

# Просмотр первых 5 строк DataFrame
print(df.head())

#Выведите информацию о данных (.info()) и статистическое описание (.describe()).
print(df.info())

print(df.describe())