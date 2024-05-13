import pandas as pd

# df = pd.read_excel(r'C:\Users\prana\Downloads\Python Class\pandas_notes\sudeep.xlsx')
# df = pd.read_csv(r'sudeep.csv')
# print(df)
# #
# print(df.shape)
# rows = df.shape[0]
# cols = df.shape[1]
# print(rows)
# print(cols)

# print(df.head(4))
# print("\n =================================== \n")
# print(df.tail(3))


# print(df[['name','salary','pincode']])

# print(type(df['age']))
# age = list(df['age'])
# print(age)
# print(type(age))

# cnt = age.count(21)
# print(cnt)


# slicing in DF
# print(df[1:6])


# create simple data frame and excel file

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# print(type(data))
# df = pd.DataFrame(data)
# print(df)
# df.to_excel(r'C:\Users\prana\Downloads\Python Class\pandas_notes\testdata.xlsx',index=False)

# df = pd.read_excel(r'C:\Users\prana\Downloads\Python Class\pandas_notes\testdata.xlsx')
# print(df)



# locate the row from DF

# print(df.loc[2])  # returns first row
# print("\n \n ", df.loc[[0, 2, 1 ]]) # returns first and sec row

#adding new column

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# print(type(data))
# df = pd.DataFrame(data)
# print(df)
# #
# print("After adding column \n")
# df['time'] = [8,9,8]
# print(df)



# print("After deleting ")
# # #delete column
# del df['duration','time']
# print(df)

# get particular index row
# print(df.iloc[2])  # prints second row of the Excel


# concatenate 2 DF

# #
# import pandas as pd
#
# df_1 = pd.DataFrame(
#   [['Somu', 68, 84, 78, 96],
#    ['Kiku', 74, 56, 88, 85],
#    ['Ajit', 77, 73, 82, 87]],
#   columns=['name', 'physics', 'chemistry', 'algebra', 'calculus'])
#
# df_2 = pd.DataFrame(
#   [['Amol', 72, 67, 91, 83],
#    ['Lini', 78, 69, 87, 92]],
#  columns=['name', 'physics', 'chemistry', 'algebra', 'calculus'])
#
# print(df_1)
# print(df_2)
#
# frames = [df_1, df_2]
# # concatenate dataframes
# df = pd.concat(frames,sort=True,ignore_index=True)
#
# # print dataframe
# print("df_1\n------\n", df_1)
# print("\ndf_2\n------\n", df_2)
# print("\ndf\n--------\n", df)

#
# # another example of concatenate

import pandas as pd

# df_1 = pd.DataFrame(
#   [['Somu', 68, 84, 78, 96],
#    ['Kiku', 74, 56, 88, 85],
#    ['Ajit', 77, 73, 82, 87]],
#   columns=['name', 'physics', 'chemistry', 'algebra', 'calculus'])
#
# df_2 = pd.DataFrame(
#   [['Amol', 72, 67, 91, 83],
#    ['Lini', 78, 69, 87, 92]],
#   columns=['name', 'physics', 'chemistry', 'geometry', 'calculus'])
#
# frames = [df_1, df_2]
#
# # concatenate dataframes
# df = pd.concat(frames, sort=True, ignore_index=True)
#
# # print dataframe
# print("df_1\n------\n", df_1)
# print("\ndf_2\n------\n", df_2)
# print("\ndf\n--------\n", df)
#
# df.to_excel(r'mergeddata.xlsx',index=False)



# get max or min value

#
# import pandas as pd
#
# mydictionary = {'physics': [68, 74, 77, 78],
#      'chemistry': [84, 56, 73, 69],
#      'algebra': [78, 88, 82, 87]}
#
# # Create DataFrame
# df_marks = pd.DataFrame(mydictionary)
# print('DataFrame\n----------')
# print(df_marks)
#
# # # Calculate max along columns
# max_data = df_marks.max()
# print('\nMaximum Value\n------')
# print(max_data)
#
#
# min_data = df_marks.min()
# print('\nminimum Value\n------')
# print(min_data)
#
#
# maxdata = df_marks['physics'].max()
# print(maxdata)

######## get rows of particular indexes

# import pandas as pd

# df = pd.DataFrame({'name':['a', 'b', 'c', 'd', 'e'],
#                    'age' :[20, 21, 20, 19, 21]})
# print(df)
# result = df.take([1, 3, 4])
# print(result)

# filter rows


import pandas as pd
#
# #initialize dataframe
# # #
# df = pd.DataFrame({'a': [2, 4, 8, 5], 'b': [2, 0, 9, 7]})
# print("\n ", df ,"\n")
# #check if the values of df['a'] are in the range(3,6)
# out = df['a'].isin(range(3,6))
#
# #filter dataframe
# filtered_df = df[out]
#
# print('Original DataFrame\n-------------------\n',df)
# print('\nFiltered DataFrame\n-------------------\n',filtered_df)


# df_1 = pd.DataFrame(
#   [['Somu', 68, 84, 78, 96],
#    ['Kiku', 74, 56, 88, 85],
#    ['Ajit', 77, 73, 82, 87]],
#   columns=['name', 'physics', 'chemistry', 'algebra', 'calculus'])
#
# out = df_1['physics'].isin(range(60,70))
# resdf = df_1[out]
#
# print(resdf)






#### another example


# import pandas as pd

#initialize dataframe
# df = pd.DataFrame({'a': [1, 4, 7, 2,7], 'b': [2, 0, 8, 7,21]})
# print(df)

#get rows where that b>4
# filtered_df = df.query('b>4')
# filtered_df2 = df.query('a==7')
#
# print('Original DataFrame\n-------------------\n',df)
# print('\nFiltered DataFrame\n-------------------\n',filtered_df)
# print('\nFiltered DataFrame\n-------------------\n',filtered_df2)
#

#
# df_1 = pd.DataFrame(
#   [['ram', 68, 84, 78, 96],
#    ['vishnu', 74, 56, 88, 85],
#    ['kiran', 77, 43, 82, 87]],
#   columns=['name', 'physics', 'chemistry', 'algebra', 'calculus'])
#
# print(df_1)
# # filtered_df = df.query('b>4')
#
#
# resdf = df_1.query('algebra >= 80')
# print(resdf)

