import numpy as np
import pandas as pd 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
#Seaborn has training datasets to work with 
#load the data
tips = sns.load_dataset('tips')
print(tips.head())
print(tips.describe())
#data for people who left a tip in the store
#Distribution plot
sns.distplot(tips['total_bill'])#it shows the distribution alogn with the kde of tthe df['column_name'](kernel density estimation)
plt.show()
#should we want the kde not to be shown we need the following
sns.distplot(tips['total_bill'], kde = False)
plt.show()
#a distribution plot is a histogram along with the kde graph
#a histogram has in the x axis the values of the column and on the y axis it has the number of instances for the range of values of x
sns.distplot(tips['total_bill'], kde = False, bins = 40)
plt.show()
#Joint plot
#it provides us with the opportunity of combinig distplots for two columns
sns.jointplot(x = 'total_bill', y = 'tip' , data = tips)
plt.show()
#a parameter kind is by default set to scatter but we can change it
sns.jointplot(x = 'total_bill', y = 'tip' , data = tips, kind = 'hex')
plt.show()
#we can also set the kind to reg to plot the linear regression line of the data
sns.jointplot(x = 'total_bill', y = 'tip' , data = tips, kind = 'reg')
plt.show()
#we can also plot the 2d kde for the two columns
sns.jointplot(x = 'total_bill', y = 'tip' , data = tips, kind = 'kde')
plt.show()
#Pair Plot
sns.pairplot(tips)#it provides scatter plots for every different two columns and for the same columns we have a histogram
plt.show()
#we can pass the argument hue = 'categorical column name' in order to color the plots based on a categorical column like sex
sns.pairplot(tips, hue = 'sex')
plt.show()
#should you change the color representation of the plot, you will affect the palettter argument 
sns.pairplot(tips, hue = 'sex', palette = 'magma')
plt.show()#also try the palette = 'coolwarm'
#Rug plot
sns.rugplot(tips['total_bill'])
plt.show()#the difference between the hist and rug plot is that the first measures how many dashes there are between two x-axis points and draws them as a bin, and as the bins are increased(up to an upper bound) the quality is rising because the range is getting smaller
#also the kernel density can be interpreted by the rug plot. the kde plot is the sum of the gaussian normal distribution for every dash of the plot.So in regions with dense rugs we expect a higher value of kde
#Kde plot
sns.kdeplot(tips['total_bill'])
plt.show()
#Categorical Plots
#Up to now we only plotted numerical columns and we will focus now on categorical plots
#Again we are going to use the tips dataset
#bar plot
sns.barplot(x = 'sex', y = 'total_bill', data = tips)
plt.show()#it will print the mean by sex of the total bill
#We use one categorical and one numerical column
#by adding an estimator argument which is an agreggate function and it is default in mean
sns.barplot(x = 'sex', y = 'total_bill', data = tips, estimator =  np.std)
plt.show()#it will print the mean by sex of the total bill
#count plot
#it resembles the way of the barplot in the estimator = count
sns.countplot(x='sex',data=tips)
plt.show()
#the y axis in this kind of plot is already set to count the occurencies of each category
#box plot
#used to see the distribution of the categorical cols
sns.boxplot(x='day', y = 'total_bill', data=tips)
plt.show()#the dots outside the plots are the outliers
#we can also add the hue as we did in scatter plots
sns.boxplot(x='day', y = 'total_bill', data=tips, hue = 'smoker')
plt.show()
#violin plot
#it is similar plot to the previous
sns.violinplot(x='day', y = 'total_bill', data=tips)
plt.show()#it shows the kde of the datapoints but is harder to interpret than boxplts and we also have the ability of adding hue and by using split we can have another "hue" which is going to be in the other half of the plot split = True
#strip plot
#it is a scatter plot between a categorical and a numerical column
sns.stripplot(x='day', y='total_bill', data = tips, jitter=True)
plt.show()#the jitter true reassures that we add a little noise to unpack the really packed data point in this kind of plot
#swarmplot
#it combines the ideas of the previous two plots
sns.swarmplot(x='day', y='total_bill', data = tips)
plt.show()#a drawback is that they dont behave well in large datasets
#advanced
sns.violinplot(x='day', y = 'total_bill', data=tips)
sns.swarmplot(x='day', y='total_bill', data = tips, color='black')
plt.show()
#factor plot
#sns.factorplot(x='day', y='total_bill', data = tips, kind = 'bar')#in the kind you can specify what type of plot you want
#we can print the correlation matrix of the dataset
#print(tips.corr())
#corr_mat = tips.corr()
#sns.heatmap(corr_mat)#it color through a colorscale the above value
#plt.show()
#to also depict the values of the correlation use annot=true and for cmap you can choose whatever you want like 'coolwarm'
#sns.heatmap(corr_mat, annot=True, cmap = 'veridis')
#plt.show()
#cluster map
#it tries to cluster hierarchically the rows and columns based on their similarities
#sns.clustermap(tips)
#plt.show()
#Grids in seaborn
flowers = sns.load_dataset('iris')
print(flowers.head())
#print the pairplot of the data
sns.pairplot(flowers)
plt.show()
#The grid is a step behind the pair plot and it gives us the freedom to choose the type of the plot we want for the upper the diaginal and the lower part of the grid
#the approach is like th OOP in the matplotlib and axes
grid = sns.PairGrid(flowers)
grid.map_upper(sns.kdeplot)
grid.map_diag(sns.distplot)
grid.map_lower(plt.scatter)
plt.show()#try also print the grid alone in order to see the empty canvas
#Facet grid
#with this type of grid we can have more control since we can plot like using hue but in the following way
gr = sns.FacetGrid(data=tips, col='time',row='somker')
gr.map(sns.distplot, 'total_bill')
plt.show()
#Regression plots
#used for linear models and their representation
sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue='sex', markers = ['o', '-'])#linear model plot
#in order to have a two different plots for males and females we can pass instead of hue the col argument and create a grid like this
sns.lmplot(x = 'total_bill', y = 'tip', data = tips,col='sex',row='smoker')
plt.show()#should you want more info than that also add hue to this 
#Styling/Font/Color
sns.set_style(style = 'whitegrid')#it determines the style of all the following plots
#remove spikes
sns.despine(left=True,bottom=True,right=True,up=True)#remove spines from all the edges of the plot
sns.set_context('poster', font_scale=1.25)#poster,notebook for determining the size of the plot


plt.show()#two lines for linear regression
