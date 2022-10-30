import csv
import matplotlib.pyplot as plt
import numpy as np

f = open("iris.csv",'r')
f1 = csv.reader(f)
the_file = list(f1)
f.close()

setosa_length1 = []
setosa_width1 = []
setosa_length2 = []
setosa_width2 = []
versicolor_length1 = []
versicolor_width1 = []
versicolor_length2 = []
versicolor_width2 = []
virginica_length1 = []
virginica_width1 = []
virginica_length2 = []
virginica_width2 = []

for i in range(1,51):
    setosa_length1.append(float(the_file[i][0]))
    setosa_width1.append(float(the_file[i][1]))
    setosa_length2.append(float(the_file[i][2]))
    setosa_width2.append(float(the_file[i][3]))
for i in range(51,101):
    versicolor_length1.append(float(the_file[i][0]))
    versicolor_width1.append(float(the_file[i][1]))
    versicolor_length2.append(float(the_file[i][2]))
    versicolor_width2.append(float(the_file[i][3]))
for i in range(101,151):
    virginica_length1.append(float(the_file[i][0]))
    virginica_width1.append(float(the_file[i][1]))
    virginica_length2.append(float(the_file[i][2]))
    virginica_width2.append(float(the_file[i][3]))

plt.subplot(231)
x = np.array(setosa_length1)
y = np.array(setosa_width1)
plt.scatter(x,y,color='blue',label='setosa')
x = np.array(versicolor_length1)
y = np.array(versicolor_width1)
plt.scatter(x,y,color='green',label='versicolor')
x = np.array(virginica_length1)
y = np.array(virginica_width1)
plt.scatter(x,y,color='red',label='virginica')
plt.legend()
plt.xlabel('Sepal_Length')
plt.ylabel('Sepal_Width')

plt.subplot(232)
x = np.array(setosa_length1)
y = np.array(setosa_length2)
plt.scatter(x,y,color='blue',label='setosa')
x = np.array(versicolor_length1)
y = np.array(versicolor_length2)
plt.scatter(x,y,color='green',label='versicolor')
x = np.array(virginica_length1)
y = np.array(virginica_length2)
plt.scatter(x,y,color='red',label='virginica')
plt.legend()
plt.xlabel('Sepal_Length')
plt.ylabel('Petal_Length')

plt.subplot(233)
x = np.array(setosa_length1)
y = np.array(setosa_width2)
plt.scatter(x,y,color='blue',label='setosa')
x = np.array(versicolor_length1)
y = np.array(versicolor_width2)
plt.scatter(x,y,color='green',label='versicolor')
x = np.array(virginica_length1)
y = np.array(virginica_width2)
plt.scatter(x,y,color='red',label='virginica')
plt.legend()
plt.xlabel('Sepal_Length')
plt.ylabel('Petal_Width')

plt.subplot(234)
x = np.array(setosa_width1)
y = np.array(setosa_length2)
plt.scatter(x,y,color='blue',label='setosa')
x = np.array(versicolor_width1)
y = np.array(versicolor_length2)
plt.scatter(x,y,color='green',label='versicolor')
x = np.array(virginica_width1)
y = np.array(virginica_length2)
plt.scatter(x,y,color='red',label='virginica')
plt.legend()
plt.xlabel('Sepal_Width')
plt.ylabel('Petal_Length')

plt.subplot(235)
x = np.array(setosa_width1)
y = np.array(setosa_width2)
plt.scatter(x,y,color='blue',label='setosa')
x = np.array(versicolor_width1)
y = np.array(versicolor_width2)
plt.scatter(x,y,color='green',label='versicolor')
x = np.array(virginica_width1)
y = np.array(virginica_width2)
plt.scatter(x,y,color='red',label='virginica')
plt.legend()
plt.xlabel('Sepal_Width')
plt.ylabel('Petal_Width')

plt.subplot(236)
x = np.array(setosa_length2)
y = np.array(setosa_width2)
plt.scatter(x,y,color='blue',label='setosa')
x = np.array(versicolor_length2)
y = np.array(versicolor_width2)
plt.scatter(x,y,color='green',label='versicolor')
x = np.array(virginica_length2)
y = np.array(virginica_width2)
plt.scatter(x,y,color='red',label='virginica')
plt.legend()
plt.xlabel('Petal_Length')
plt.ylabel('Petal_Width')

plt.show()