import numpy as np
import pandas as pd
#LESSON 7
#Series
#Series is build on top of a numpy arrays and the difference is that we can reference by thei labels
labels = ['a', 'b','c']
grades = [10,20,30]
arr = np.array(grades)
dict = {labels[0] : grades[0], labels[1]:grades[1], labels[-1] : grades[-1]}
print(dict)
ser = pd.Series(data = grades)
print(ser)
ser = pd.Series(data = grades, index = labels)
print(ser)
#Series(data,index)
#We can also pass a numpy array in the position of the data
#Also we can pass a dictionary and the value is the data and the key is the label
#The argument of series can have any type they want
#It is used like a hash table and it is pretty fast at looking ans finding
ser1 = pd.Series(['NICK', 'MARIA', 'KOSTAS'], [12, 45, 75])
print(ser1)
ser2 = pd.Series(['NICK', 'TZANIS', 'KOSTAS'], [12, 45, 75])
print(ser2)
#The retrieval of info is done by using dictionary techniques
print(ser1[12])
#the key value is the index
#The + in the series is like a full outer join in in databases
print(ser1+ser2)
#LESSON 8
#Dataframes(IMPORTANT)
np.random.seed(1)#get the same random numbers every time
df = pd.DataFrame(np.random.randn(5,4), ['A','B','C','D','E'], ['W','X','Y','Z'])#data,index,columns
print(df)
#Each column is a series which they share a common index
#Indexing
print(df['W'])#first index the column then the row
print(df['W']['A'])
#print(df[:]['A']) not allowed
#On the otther hand borrowed by sql we can access a column like this
print(df.W)
#to get more than one column we need to pass a list of columns
print(df[['W', 'Z']])
#create a new column
df['color'] = ['Blue', 'Red', 'Black','Yellow','Purple']
print(df)
#in order to delete a column or a row we need to specify the axis on whcih the deletion is done
#axis = 0->rows axis=1->columns
print(df.drop('color', axis = 1))#again if we want to delete more than one we pass in a list with the name of the columns
print(df.drop('A', axis = 0 ))# the default value of axis = 0
#Note that the dataframe hasn't change until we say so
#print(df['A'])
df.drop('color', axis = 1, inplace = True)
print(df)
print(df.drop('A', axis = 0, inplace = True))
#to get the shape of the df use the shape method
print(df.shape)
#Selecting rows of a dataframe
#print(df['B'])
print(df.loc['B'])
print(df.iloc[2])#index lookup
#Slicing a dataframe
#use loc and first slice the rows and the columns
print(df.loc['B', 'Y'])#locating an element of the dataframe
#A subset can be regained by a list
print(df.loc[['B', 'C'],['X', 'Y']])
#the same can be done with the iloc mehtod
print(df.iloc[0:2,1:3])#again the last element is excluding
#Remember index=rows
#LESSON 9
#as we did in the numpy arrays we can conditional select things from our dataste and the result is a boolean array which we then use to grab the desired info
print(df>0)
print(df[df>0])
#Where the boolean value happens to be flse then the result of print is NaN
#we use the above to filter index lets see the following example
print(df)
df['Age'] = [45 ,78, 95, 87]
print(df)
#lets say that we want to grab the data where the age is between sound bounds
#the result will only contain rows that match this codition
#print(df[50<df['Age']<90]) this is not allowed and we should use and
#we get only the C,E rows
print(df[(df['Age'] > 50) & (df['Age'] < 90)])
#the result is a dataframe
#we can also grab columns from the result dataframe
print(df[df['Age']>64][['Y', 'X']])
#should we want to get the initial rnaking of the dtataframe we use the method reset_index() and the previous index becomes a column
print(df.reset_index())
#if we want the change to be permanent we use inplace = True
#setting the index(new)
#if we want age to be the index we can use the set_index
print(df.set_index('Age'))
#LESSON 10
#like comparch or databses we can have multiindexing an outside smaller index and an inside more detailed one
out_ind = ['A', 'A', 'A', 'B', 'B', 'B']
in_ind = [1 ,2 ,3 ,1, 2, 3]# A, B may be male/female and 1 2 3 may be chef, sous-chef and chef_B
hier_index = list(zip(out_ind,in_ind))
print(hier_index)#this create a list of tuples by combinig the elements bitwsely from the two lists
hier_index = pd.MultiIndex.from_tuples(hier_index)#create a multilevel index using tuples
df = pd.DataFrame(np.random.randn(6,2), hier_index, ['COL_1', 'COL_2'])
print(df)
#Dealing with multilevel indexing
print(df.loc['A'])#take the smaller subset/subdf for A
print(df.loc['B'].loc[2]['COL_1'])#Double loc because we have two levels
#We can also name indexes by using the following
df.index.names = ['LETTERS', 'NUMS']
print(df)
#only in multilevel index
print(df.xs('A'))#cross-section method
print(df.xs(1,level='NUMS'))
#LESSON 11
#We can also see a dictionary as a dataframe if the first has keys and their values are lists
dict = {'a':[1,2,4, np.nan], 'b':[4,np.nan,6,5], 'c':[2,3,4,10]}
print(dict)
df = pd.DataFrame(dict)
print(df)
#Generally in data scinece and machine learning we don't want unknown values
#So in this lesson we are going to see ways to handle them
#.dropna
print(df.dropna())#it will drop every row that has one or more null values
print(df.dropna(axis = 1))#same for the column but use of axis 
#if we want to drop a column or a row to have more than threshold nan values in order them to be deprecated
print(df.dropna(thresh = 2, axis = 0))
#Filling instead of dropping them
print(df.fillna(value="FILLED"))
#the most common is to use the mean of the column or the median
print(df['a'].fillna(value = df['a'].mean()))
#Groupby
#Groupby allows you to group together rows based off a column and perform aggregate functions in them like sql
#it ignores every non numerical columns when mean or std are applied
#LESSON 11
#Lets say that we have three dfs we can concatenate thm on both columns and indexes and we should reassure that the dimensions match on the axis of the concat
#pd.concat([list of dataframes to concat], axis = 0 or 1)
#Merging is the same with sql
#pd.merge(df1, df2, how = 'inner', on = 'key')how is the kind of join and the one is the name of the column that we want the match to happen
#LESSON 12
# Sample data
data = {
    'CustomerID': [f'CUST{i+1}' for i in range(20)],
    'Name': [
        'Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ivy', 'John',
        'Kathy', 'Leo', 'Mona', 'Nina', 'Oscar', 'Paul', 'Quincy', 'Rachel', 'Steve', 'Tina'
    ],
    'Age': [25, 34, 45, 23, 31, 29, 38, 40, 27, 33, 36, 30, 41, 22, 35, 28, 26, 32, 39, 24],
    'Gender': [
        'F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'F', 'M',
        'F', 'M', 'F', 'F', 'M', 'M', 'M', 'F', 'M', 'F'
    ],
    'PurchaseAmount': [
        250.50, 340.75, 125.60, 430.90, 315.25, 290.80, 188.50, 210.65, 275.40, 330.15,
        289.35, 400.25, 150.45, 175.20, 450.00, 380.50, 310.60, 260.55, 490.90, 299.70
    ]
}

# Create the DataFrame
df = pd.DataFrame(data)

print(df)
#Print the first rows of it 
print(df.head(n=7))
#print some statistics of the data
print(df.shape)
print(df.describe())
print(df.info)
#Print the names of the columns
print(df.columns)
#find the unique values of a column
print(df['Gender'].unique())
#find all the values of the column
print(df['Gender'].value_counts())
#apply method
#We can use aggregate functions in columns of the df like the following
print(df['Age'].sum())
#but with apply we can use any custom funtion we want
def double_age(x):
    return x+x
print(df['Age'].apply(double_age))
#We can also use prebuilt expression like len
#and we commonly apply lambda functions like the following one
print(df['Age'].apply(lambda x : x**2))
#df.drop([name of columns to drop], inplace = T or F, axis = 0 or 1)
#Sorting 
print(df.sort_values('Age', inplace = True))
#finding null values
print(df.isnull())
#Pivoting like excel
#df.pivot_table(values = 'name of column', index = [list of cols], columns = [])
#in order to read a csv file we have the following
#df = pd.read_csv('path')
#In order to save a df to a given form we use the below 
#df.to_typefile(Name of file, index = False), the second arg tells us to not save the index into the file

