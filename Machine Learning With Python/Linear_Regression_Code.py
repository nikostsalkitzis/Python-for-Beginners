import numpy as np
import pandas as pd 
import matplotlib 
matplotlib.use('Tkagg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error
sales = pd.read_csv('Real_Estate.csv')
#Data Cleaning 
print(sales.info)
print(sales.describe())
print(sales.head())
print(sales.isnull().sum())
print(sales.columns)
"""
['No', 'X1 transaction date', 'X2 house age',
       'X3 distance to the nearest MRT station',
       'X4 number of convenience stores', 'X5 latitude', 'X6 longitude',
       'Y house price of unit area']
"""
sales = sales.rename(columns={"No": "No", "X1 transaction date": "Transaction_Date", "X2 house age": "House_Age",
    "X3 distance to the nearest MRT station": "MRT_Distance", "X4 number of convenience stores": "Convenient_Stores",
    "X5 latitude": "Lat", "X6 longitude": "Long", "Y house price of unit area": "Price"})
print(sales.columns)
#I renamed the columns in order to better visualize their meaning
#useful plots
sns.pairplot(sales)
plt.show()
sns.distplot(sales['Price'], bins=50, color = 'red')
plt.show()
#Create an instance/object of the model
lm = LinearRegression()
#Create the features and the target columns
X = sales[['Transaction_Date', 'House_Age','MRT_Distance','Convenient_Stores', 'Lat', 'Long']]
y = sales['Price']
#split the dataset into train and test
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3, random_state=17)
#train the model
lm.fit(X_train,y_train)
#Print the "slopes" of each features
slopes = lm.coef_
print(slopes)
#print the intercept with the x axis
intercept = lm.intercept_
print(intercept)
#Predictions
predictions = lm.predict(X_test)
#In order to see if our model performs well we need to scatter them along with the y_true values
plt.figure(1,figsize=(10,8))
plt.scatter(predictions,y_test,color='red')
plt.xlabel('Predictions')
plt.ylabel('y_test')
plt.title('Performance Plot')
plt.show()
#should we see the result we can see a y=ax behaviour along with some noise which may occur due to outliers and bad scaling
#Metrics Evaluation
print("The MAE of the above problem is {}.".format(mean_absolute_error(y_test,predictions)))
print("The MSE of the above problem is {}.".format(mean_squared_error(y_test,predictions)))
print("The RMSE of the above problem is {}.".format(np.sqrt(mean_squared_error(y_test,predictions))))

