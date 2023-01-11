import pandas as pd
import matplotlib.pyplot as plt

initial_data = pd.read_csv("vgsales-12-4-2019.csv",index_col='Rank')

initial_data['total_sale'] = initial_data['Total_Shipped'].to_numpy(dtype='float32',na_value='0') + initial_data['Global_Sales'].to_numpy(dtype='float32',na_value='0')

data = initial_data.loc[initial_data['total_sale'] > 0.001]
data.info()

count_Platform = data['Platform'].value_counts()
count_Publisher = data['Publisher'].value_counts()
count_Year = data['Year'].value_counts()

count_Publisher = count_Publisher.head(10)  #截取出产游戏前十名公司的数据
count_Publisher = pd.Series([1027 ,949 , 822 , 767,  753,  718,  711,  631,  626,  534],index=['Activision', 'Ubisoft', 'Electronic Arts', 'Konami', 'Nintendo', 'THQ',
       'Sega', 'Unknown', 'Sony', 'EA Sports'])



'''
#获取生产游戏数量前十名公司的数据并绘制柱状图
plt.bar(count_Publisher.index,count_Publisher.values)
plt.xticks(fontsize=6,rotation=20)
for a, b in zip(count_Publisher.index,count_Publisher.values):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

plt.figure(figsize=(15,20))
plt.show()

'''

'''
#为生产游戏数量前十名的公司绘制饼状图
plt.pie(count_Publisher.values,labels=count_Publisher.index,explode=[0.1,0,0,0,0.1,0,0,0,0,0])
plt.show()
'''

"""#截取平台前十名的数据
count_Platform = count_Platform.head(10)"""

'''
#平台前十名柱状图
plt.bar(count_Platform.index,count_Platform.values)
plt.xticks(fontsize=6,rotation=20)
for a, b in zip(count_Platform.index,count_Platform.values):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

plt.figure(figsize=(15,20))
plt.show()
'''

"""count_Platform = pd.Series([15,14,14,9,9,8,8,8,6,5],index=['DS', 'PS2', 'PC', 'PS3', 'Wii', 'PSP', 'X360', 'PS', 'PS4', 'GBA'])

plt.pie(count_Platform.values,labels=count_Platform.index,autopct="%1.1f%%",explode=[0,0.1,0,0,0,0.1,0,0,0,0])
plt.show()





#筛选出98年到08年的数据
data_from98_to08 = data.loc[(data['Year'] >= 1998) & (data['Year'] <= 2008)]

count_Platform_from98_to08 = data_from98_to08['Platform'].value_counts()
count_Publisher_from98_to08 = data_from98_to08['Publisher'].value_counts()
count_Year_from98_to08 = data_from98_to08['Year'].value_counts()

count_Publisher_from98_to08 = count_Publisher_from98_to08.head(10)

count_Publisher_from98_to08 = pd.Series([514,499 ,488, 473, 445, 366, 350, 346, 325, 239],index=['Konami', 'Activision', 'THQ', 'Electronic Arts', 'Ubisoft', 'Sega',
       'Sony', 'Nintendo', 'EA Sports', 'Unknown'])

#统计图的制作
plt.bar(count_Publisher_from98_to08.index,count_Publisher_from98_to08.values)
plt.xticks(fontsize=6,rotation=20)
for a, b in zip(count_Publisher_from98_to08.index,count_Publisher_from98_to08.values):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
plt.figure(figsize=(15,20))
plt.show()

plt.pie(count_Publisher_from98_to08.values,labels=count_Publisher_from98_to08.index,explode=[0,0,0.1,0,0,0,0,0.1,0,0])
plt.show()

count_Platform_from98_to08 = count_Platform_from98_to08.head(10)
plt.bar(count_Platform_from98_to08.index,count_Platform_from98_to08.values)
plt.xticks(fontsize=6,rotation=20)
for a, b in zip(count_Platform_from98_to08.index,count_Platform_from98_to08.values):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

plt.figure(figsize=(15,20))
plt.show()

count_Platform_from98_to08 = pd.Series([24,14,10,10,9,7,6,6,5,4], index=['PS2', 'DS', 'GBA', 'XB', 'PS', 'PC', 'GC', 'PSP', 'Wii', 'X360'])
plt.pie(count_Platform_from98_to08.values,labels=count_Platform_from98_to08.index,autopct="%1.1f%%",explode=[0,0.1,0,0,0,0.1,0,0,0,0])
plt.show()"""

