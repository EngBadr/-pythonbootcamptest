import pandas as pd

#create Series call it (Data) with the values 'a','b','d','u' and 'l'
print('create Series call it (Data) with the values \'a\',\'b\',\'d\',\'u\' and \'l\'')
data=['a','b','d','u', 'l']

s=pd.Series(data)

print(s)

#change index to 3,6,9,12, and 15 for (data)
print('change index to 3,6,9,12, and 15 for (data)')
s=pd.Series(data,index=[3,6,9,12,15])

print(s)

#change index to client1, client2, client3, client4 and client5 for (data)
print('change index to client1, client2, client3, client4 and client5 for (data)')
s=pd.Series(data,index=['client1', 'client2', 'client3', 'client4' , 'client5'])
print(s)

#create a dataframe (D) with the followin values
D=pd.DataFrame({'Name':['Ali','Ahmed','Nora'],'Age':[55,15,40]})
print(D)

#Mean of ages 
print('Mean of ages  ')
print(D['Age'].mean())