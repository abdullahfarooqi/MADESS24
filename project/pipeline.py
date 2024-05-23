import pandas as pd

df = pd.read_csv('https://www.umweltbundesamt.de/api/air_data/v2/measures/csv?data%5B0%5D%5Bst%5D=1562&data%5B0%5D%5Bco%5D=3&data%5B0%5D%5Bsc%5D=2&date_from=2024-01-01&time_from=1&date_to=2024-12-31&time_to=24&lang=en', sep=';')
## df.columns.values[0] = 'name'
df_filtered_measure = df[df['Measure value'] != '-']
df_filtered_cols = df_filtered_measure.drop(columns=['Station code', 'Station setting', 'Station type'])
df_filtered_cols.to_sql('Ozone', 'sqlite:///project.sqlite', if_exists='replace', index=False)

df = pd.read_csv('https://www.umweltbundesamt.de/api/air_data/v2/measures/csv?data%5B0%5D%5Bst%5D=1562&data%5B0%5D%5Bco%5D=5&data%5B0%5D%5Bsc%5D=2&date_from=2024-01-01&time_from=1&date_to=2024-12-31&time_to=24&lang=en', sep=';')
## df.columns.values[0] = 'name'
df_filtered_measure = df[df['Measure value'] != '-']
df_filtered_cols = df_filtered_measure.drop(columns=['Station code', 'Station setting', 'Station type'])
df_filtered_cols.to_sql('NO2', 'sqlite:///project.sqlite', if_exists='replace', index=False)