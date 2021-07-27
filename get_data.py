import pandas as pd
import csv
import datetime


df = pd.read_excel("C:\\nes\\Master_File\\Master.xlsx", sheet_name='Iraq1')
df['code'] = df['Health admin']
df['Confirmed'] = df['New Cases']
df['Deaths'] = df['New Deaths']
df['Cumulative_Cases'] = df['Confirmed'].cumsum()
df['Cumulative_Deaths'] = df['Deaths'].cumsum()


df['code'].replace(to_replace=['ANBAR','BABYLON','BAGHDAD-KARKH','BAGHDAD-RESAFA','BASRAH','DAHUK','DIWANIYA',
                    'DIYALA','ERBIL','KERBALA','KIRKUK','MISSAN','MUTHANNA','NAJAF','NINEWA','SALAH AL-DIN','SULAYMANIYAH',
                    'THI-QAR','WASSIT'],
                    value=['Anbar','Babylon','Baghdad-Karkh','Baghdad-resafa','Basrah','Dahuk','Qadissiya',
                    'Diyala','Erbil','Kerbala','Kirkuk','Missan','Muthanna','Najaf','Ninewa','Salah al-Din','Sulaymaniyah',
                    'Thi-Qar','Wassit'], inplace = True)

locations = pd.read_csv('C:\\project\\gov_xy\\iraq.csv')
locations['code'] = locations['admin1Name']
locations['Latitude'] = locations['x']
locations['Longitude'] = locations['y']


result = pd.merge(locations, df, on='code', how='inner')

result.drop(['Health admin','admin1Name','x','y','New Cases','Cumulative Cases','New Deaths','Cumulative Deaths'], inplace=True, axis=1)

today = datetime.date.today().strftime("%Y-%m-%d")

x = '2021-07-27'

corect_date = result[result['Date'] == x]
#corect_date.drop(['Health admin','New Cases','Cumulative Cases','New Deaths','Cumulative Deaths'], inplace=True, axis=1)
corect_date.to_csv("C:/2.csv", index=False)
print(today)
