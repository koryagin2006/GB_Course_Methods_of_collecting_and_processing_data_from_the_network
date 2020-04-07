import csv
import pandas as pd
from requests import get

url = 'https://data.gov.ru/opendata/7707778246-grls'
data = get(url,)
f = open('data.csv','w',encoding='UTF-8')
f.write(data.text)
f.close()

# with open('data.csv','r', encoding='UTF-8') as f:
#     reader = csv.DictReader(f, delimiter=',')
#     fields_names = reader.fieldnames
#     # print(fields_names)
#     for row in reader:
#         print(row['Наименование показателя'], row['% исполнения'])

# data_frame = pd.read_csv(url,sep=',')
# result = data_frame[data_frame['% исполнения'] > 20]
# print(result)




