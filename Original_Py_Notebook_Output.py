#!/usr/bin/env python
# coding: utf-8

# # Linear Regression in Python

# In[5]:


#Reading the csv


# In[1]:


import csv #importing the csv file
with open('regression_data.csv', 'r') as lr_data: #opening the csv file and renaming it
    csv_reader = csv.reader(lr_data) #reading the csv file
    for row in csv_reader:
        print(row) #for every single row of our CSV file, print it


# In[3]:


import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np #these are all necessary packages for the graph and the line

if len(sys.argv) != 4:
    print("Enter file name, your x variable, and your y variable after the script name: python linear_regression_python.py <filename> <x_var> <y_var>")
    sys.exit(1)

filename = sys.argv[1]
x_var = sys.argv[2]
y_var = sys.argv[3]

# In[4]:


data = pd.read_csv('filename') #re-reading the csv, using pandas to make it more malleable for data analysis


# In[6]:


x_lr = np.array(data.x_var) #creating a variable out of an array of the x values in the CSV file
y_lr = np.array(data.y_var) #creating a variable out of an array of the y values in the CSV file

print(x_lr) 
print (y_lr) #This is just another way to print the CSV file


# In[8]:


plt.scatter(x_lr, y_lr, color='k') #creates the scatterplot of the data using matplotlib and the two created arrays for the data
plt.title(f'{y_var} vs {x_col}') #title of the plot
plt.xlabel(x_var) #the title of the x axis
plt.ylabel(y_var) #the title of the y axis
plt.show()


# In[14]:


np.polyfit(x_lr, y_lr, 1) #using the polyfit function in numpy, with the x data and the y data and the 1 saying its a linear line, the slope and intercept for the linear regression line are printed


# In[20]:


plt.scatter(x_lr, y_lr, color='k') #creates the scatterplot of the data using matplotlib and the two created arrays for the data
plt.title(f'{y_var} vs {x_col}') #title of the plot
plt.xlabel(x_var) #the title of the x axis
plt.ylabel(y_var) #the title of the y axis
slope, intercept = np.polyfit(x_lr, y_lr, 1) #creating variables for slope and intercept using the numpy function
abline_values = [slope * x + intercept for x in x_lr] #creates the line using slope and intercept previously calculated
plt.plot(x_lr, abline_values, color='red') #plotting the line itself with the x axis and the y values
plt.show()


# In[13]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(data[[x_var]], data[[y_var]]) #this is the method we learned in class, using sklearn to model the linear regression


# In[16]:


plt.plot(data[x_var], model.predict(data[[x_var]]), color='k') #creates the scatterplot of the data using matplotlib and the two created arrays for the data
plt.title(f'{y_var} vs {x_col}') #title of the plot
plt.xlabel(x_var) #the title of the x axis
plt.ylabel(y_var) #the title of the y axis
plt.show() #using the code we learned in class, this just plots the line itself. Not terribly useful


# In[21]:


plt.scatter(x_lr, y_lr, color='b') #the plot itself
plt.plot(data[x_var], model.predict(data[[x_var]]), color='k') #The line on the plot
plt.title(f'{y_var} vs {x_col}') #title of the plot
plt.xlabel(x_var) #the title of the x axis
plt.ylabel(y_var) #the title of the y axis
slope, intercept = np.polyfit(x_lr, y_lr, 1) #creating variables for slope and intercept using the numpy function
abline_values = [slope * x + intercept for x in x_lr] #creates the line using slope and intercept previously calculated
plt.plot(x_lr, abline_values, color='red') #plotting the line itself with the x axis and the y values
plt.savefin("linear_regression_python_output.png")
plt.show()


# In[19]:


model.score(data[[x_var]], data[[y_var]]) #Outputs the R squared value


# In[ ]:




