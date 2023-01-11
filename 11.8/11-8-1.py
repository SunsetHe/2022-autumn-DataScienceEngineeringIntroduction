import pymysql
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

db = pymysql.connect(host = "cdb-r2g8flnu.bj.tencentcdb.com", port = 10209, user
= "dase2020", password = "dase2020", database = "dase_intro_2020")
cursor = db.cursor()
sql = 'select * from SH_Grade;'
cursor.execute(sql)
result = cursor.fetchall()

with open('SH_Grade.csv','w',newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['id','StuId','Class','Sex','CHI611','MATH611','ENG611','CHI612','MATH612','ENG612','CHI621','MATH621','ENG621','CHI622','MATH622','ENG622','CHI711','MATH711','ENG711','CHI712','MATH712','ENG712','CHI721','MATH721','ENG721','CHI722','MATH722','ENG722','CHI811','MATH811','ENG811','PHY811','CHI812','MATH812','ENG812','PHY812','CHI821','MATH821','ENG821','PHY821','CHI822','MATH822','ENG822','PHY822','CHI911','MATH911','ENG911','PHY911','CHE911','CHI912','MATH912','ENG912','PHY912','CHE912','CHI921','MATH921','ENG921','PHY921','CHE921'])
    for row in result:
        row = list(row)
        row.insert(2,row[1][0])
        writer.writerow(row)


data = pd.read_csv('SH_Grade.csv')
print('处理前数据条目：',data.shape[0])
data = data.drop_duplicates(subset=["StuId"])
print('处理后数据条目：',data.shape[0])

print("处理前数据条目：",data.shape[0])

data = data.dropna(thresh=47)
print('处理后数据条目：',data.shape[0])

data['Sex'] = data['Sex'].fillna(method='ffill')
data.loc[:,'CHI611':] = data.loc[:,'CHI611':].fillna(data.loc[:,'CHI611':].median())

data.loc[:,'CHI611':].describe().loc['max']

data[['CHI822','MATH822','ENG822']] = data[['CHI822','MATH822','ENG822']] / 120 * 100
data[['CHI911','MATH911','ENG911','CHI912','MATH912','ENG912','CHI921','MATH921','ENG921']] = data[['CHI911','MATH911','ENG911','CHI912','MATH912','ENG912','CHI921','MATH921','ENG921']] / 150 * 100
data[['PHY911','PHY921']] = data[['PHY911','PHY921']] / 0.9
data[['CHE911','CHE921']] = data[['CHE911','CHE921']] / 0.6

boy_by_class = data.loc[data['Sex'] == 'M'].groupby('Class')['StuId'].count()
girl_by_class = data.loc[data['Sex'] == 'F'].groupby('Class')['StuId'].count()
plt.bar(boy_by_class.index,boy_by_class.values,label='Boy')
plt.bar(girl_by_class.index,girl_by_class.values,bottom=boy_by_class.values,label='Girl')
plt.legend()
plt.show()

a13_chi_grade = data.loc[data['StuId'] == 'A13'][['CHI611','CHI612','CHI621','CHI622','CHI711','CHI712','CHI721','CHI722','CHI811','CHI812','CHI821','CHI822','CHI911','CHI912','CHI921']]
a15_chi_grade = data.loc[data['StuId'] == 'A15'][['CHI611','CHI612','CHI621','CHI622','CHI711','CHI712','CHI721','CHI722','CHI811','CHI812','CHI821','CHI822','CHI911','CHI912','CHI921']]
x = [t[3:] for t in a13_chi_grade.columns]
y1 = a13_chi_grade.values[0]
y2 = a15_chi_grade.values[0]

plt.figure(dpi=100)
plt.plot(x,y1,label='A13')
plt.plot(x,y2,label='A15')
plt.show()

data_8 = data.query('ENG721 < 60 or CHI721 < 60')
data_8 = data_8[['StuId','Class','ENG721','CHI721']]
print(data_8)

data_9a = data.loc[(data['Class'] == 'A')]
data_9c = data.loc[(data['Class'] == 'C')]
data_9a = data_9a[['CHI622','MATH622','ENG622']]
data_9c = data_9c[['CHI622','MATH622','ENG622']]

print('Mean of class A:\n',data_9a.mean())
print('Mean of class C:\n',data_9c.mean())
print('var of class A:\n',data_9a.var())
print('var of class C:\n',data_9c.var())

data_8.to_csv('task8.csv',index=0)