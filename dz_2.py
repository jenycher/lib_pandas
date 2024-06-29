import pandas as pd

# Загрузка данных из CSV-файла в DataFrame
file_path = 'dz.csv'
df = pd.read_csv(file_path)

# Проверка первых нескольких строк
print(df.head())

df.dropna(inplace=True)
print(df)

# Вычисление средней зарплаты по городу
average_salary_by_city = df.groupby('City')['Salary'].mean()

# Вывод результата
print(average_salary_by_city)