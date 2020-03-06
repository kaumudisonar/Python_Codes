import pandas as pd


# #Data Frame
# data=[1,25,89,65]
# df=pd.DataFrame(data)
# print(df)

# data=[['PPA',4],['LB',3],['OS',2],['PYTHON',3.5],['ANGULAR',4]]
# df=pd.DataFrame(data,columns=['Name','Duration'])
# print(df)

# data={'Name':['PPA','LB','OS','PYTHON','ANGULAR'],'Duration':[3,5,2,4,4]}
# df=pd.DataFrame(data)
# print(df)

# data={'one':pd.Series([1,2,3],index=['a','b','c']),
       # 'two':pd.Series(['a','b','c'],index=[1,2,3]) }
# df=pd.DataFrame(data)
# print(df)
# writer=pd.ExcelWriter('MarvellousPandas.xlsx',engine='xlsxwriter')
# df.to_excel(writer)
# writer.save()


#Panel
df1={'one':pd.Series([1,2,3],index=['a','b','c']),
       'two':pd.Series(['a','b','c'],index=[1,2,3]) }
df2={'three':pd.Series(['c','d','e'],index=[4,5,6]),
       'four':pd.Series(['x','y','z'],index=[7,8,9]) }
data={'item1':df1 , 'item2':df2}
panel=pd.Panel(data)
df=panel.to_frame()
print(df)