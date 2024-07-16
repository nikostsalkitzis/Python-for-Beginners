import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#Altough for histograms and for statistical plots we use seaborn
#pandas can also provide some of them
# Set the seed for reproducibility
np.random.seed(42)

# Create a DataFrame with random data
df = pd.DataFrame({
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.rand(10),
    'D': np.random.rand(10)
})

print(df)
#Histogram of a column
df['A'].hist(bins = 30)#you can change the argument
#should you like more the seaborn lib you can import it instead of matplotlib and have the analogous results
plt.show()
df['B'].plot(kind='hist', bins=100)
#Another way of plotting the histogram is
#df.plot.hist(bins = val)
#Another plot is the area one
df.plot.area()
plt.show()
#the area plot is the points of each numerical column connected together and then filled the are below them with a given color
#Bar plot
df.plot.bar()
plt.show()
df.plot.bar(stacked = True)
plt.show()#the stacked is having a more compact format to the output console
#line Plot especially useful for timeseries
df.plot.line(x = 'A', y = 'B')#due to the randomness of the data not a "nice" one
plt.show()
#scatter plot
df.plot.scatter(x = 'A', y  = 'B')
plt.show()
#you can color the scatter plot by using the other column and encorporate much more info like the one follwoing
df.plot.scatter(x = 'A', y = 'B', c = 'C', cmap = 'coolwarm')
plt.show()
#instead of color u can also use the size like the below code does
df.plot.scatter(x = 'A', y = 'B',s = df['C'])
plt.show()#due tp the smalle size we can have s = s*1000
df.plot.scatter(x = 'A', y = 'B',s = df['C']*1000)
plt.show()#due tp the smalle size we can have s = s*1000
#box plot
df.plot.box()
plt.show()
#density plot
df.plot.kde()
plt.show()


