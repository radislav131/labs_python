import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import axis, table
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('D:\csv\weatherAUS.csv',sep = ',',encoding ='latin 1',dayfirst = True,parse_dates = ['Date'],index_col = 'Date')


#1. Посчитать минимальное, максимальное, среднее, медиану по каждому числовому полю.
#Метод частный
dfcol=df.select_dtypes(include=[np.number]).columns.tolist()

for i in range(len(dfcol)):
    print(df[dfcol[i]].max())
    print(df[dfcol[i]].min())
    print(df[dfcol[i]].mean())
    print(df[dfcol[i]].median(),'\n')

#Мой метод
""""def is_number(s):
    try:
        float(s)
        return True
   "" except ValueError:
        return False
"for i in range (23):
    if is_number(df[dfcol[i]][0])==True:
  "      print(df[dfcol[i]].max())
 """


 #2. Сгруппировать данные по одному из полей, посчитать сумму(среднее) для каждой группы, отсортировать группы по возрастанию(убыванию).
 # Отобразить гистограмму средних значений групп.\
gg=df.groupby('RainToday')
res = gg[['MinTemp','MaxTemp']].agg([np.mean])
print(gg.apply(lambda x: x.sort_values('MinTemp',ascending = False)))
print(res)
res.plot.bar()
plt.show()
#print('Среднее:','\n',res)
#print('Отсортированные группы','\n',res.apply(lambda x: x.sort_values(['MinTemp','MaxTemp'],ascending = False)))



       
#3. Посчитать минимальное, максимальное, среднее, медиану по какому-либо полю, предварительно отфильтровав значения
filtr = df.query('RainToday == "Yes"')
print('Filtr = ','\n',filtr)
print(filtr['MinTemp'].min())
print(filtr['MinTemp'].max())
print(filtr['MinTemp'].mean())
print(filtr['MinTemp'].median())


#4. Построить график(и) (гистограмму(ы)) для средних значений групп по отфильтрованным данным.
dff = df.query('RainToday == "Yes"  and RainTomorrow =="No" and Location =="Albury"')
l_list = []
for i in range(len(dfcol)):
    l_list.append(dff[dfcol[i]].mean())
x = range(len(l_list))
ax = plt.gca()
ax.bar(x,l_list)
plt.show()


#5. Построить перекрестную выборку по набору данных 
#(дежурный вариант: столбцы – минимальное, максимальное, среднее, медиану по каждому числовому полю; строки – названия полей). 
#Построить график этого чуда (3d-гистограмму в частном случае)
perekrest = df[(df['MinTemp'] > 22)&(df['MaxTemp'] < 33)&(df['MinTemp'] < 27)&(df['MaxTemp'] > 25)]
perekrest['MinTemp'] = round(perekrest['MinTemp'])
perekrest['MaxTemp'] = round(perekrest['MaxTemp'])

tab = perekrest.pivot_table('Rainfall','MinTemp','MaxTemp','mean',fill_value=0)
fig = plt.figure(figsize=(15,8))
ax = Axes3D(fig)
print(tab)
x_pos = np.arange(tab.shape[0])
y_pos = np.arange(tab.shape[1])
print(y_pos)
xpos, ypos = np.meshgrid(x_pos, y_pos)
xpos = xpos.flatten()
ypos = ypos.flatten()

zpos=np.zeros(tab.shape).flatten()

zpos=np.zeros(tab.shape).flatten()

dx = 0.8
dy = 0.8
dz = tab.values.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
ax.w_xaxis.set_ticks(x_pos+dx/2)
ax.w_xaxis.set_ticklabels(tab.index)
ax.w_yaxis.set_ticks(ypos+dy/2)
ax.w_yaxis.reset_ticks()
ax.w_yaxis.set_ticks(y_pos+0.4)
ax.w_yaxis.set_ticklabels(tab.columns)

ax.set_xlabel('MinTemp')
ax.set_ylabel('MaxTemp')
ax.set_zlabel('Rainfall')

plt.show()


