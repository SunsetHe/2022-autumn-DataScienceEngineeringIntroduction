import pandas as pd
import matplotlib.pyplot as plt

initial_data = pd.read_csv("vgsales-12-4-2019.csv",index_col='Rank')

initial_data['total_sale'] = initial_data['Total_Shipped'].to_numpy(dtype='float32',na_value='0') + initial_data['Global_Sales'].to_numpy(dtype='float32',na_value='0')

data = initial_data.loc[initial_data['total_sale'] > 0.001]

sum_list = []

for i in range(1999,2019):
    data_thisyear = data.loc[data['Year'] == i]
    sum_thisyear = data_thisyear['total_sale'].sum()
    sum_list.append(sum_thisyear)
print(sum_list)

x = range(1999,2019)
y = sum_list
plt.plot(x,y)
plt.show()



count_genre = data['Genre'].value_counts()
count_genre = count_genre.head(10)

total = [1496,1464,904,505,1142,1340,806,470,999,512]
fig,ax = plt.subplots()
ax.bar(count_genre.index,count_genre.values)
ax.plot(count_genre.index,total,color='r')
plt.xticks(fontsize=6,rotation=20)


plt.show()


print(count_genre)

newlist = [0.5,0.57,0.4,0.27,0.63,0.86,0.56,0.41,0.88,0.54]
plt.bar(count_genre.index,newlist)
plt.xticks(fontsize=6,rotation=20)
plt.show()