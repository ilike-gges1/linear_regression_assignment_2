#!/usr/bin/env python
# coding: utf-8

# # Linear Regression in Python

# In[5]:


#Reading the csv


# In[1]:



import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np #these are all necessary packages for the graph and the line

if len(sys.argv) != 4:
    print("Enter file name, your x variable, and your y variable after the script name: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_var = sys.argv[2]
y_var = sys.argv[3]

# In[4]:




data = pd.read_csv(filename) #re-reading the csv, using pandas to make it more malleable for data analysis


import csv #importing the csv file
with open(filename, 'r') as lr_data: #opening the csv file and renaming it
    csv_reader = csv.reader(lr_data) #reading the csv file
    for row in csv_reader:
        print(row) #for every single row of our CSV file, print it



# In[8]:


plt.scatter(data[[x_var]], data[[y_var]], color='b') #creates the scatterplot of the data using matplotlib and the two created arrays for the data
plt.title(f'{y_var} vs {x_var}') #title of the plot
plt.xlabel(x_var) #the title of the x axis
plt.ylabel(y_var) #the title of the y axis
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(data[[x_var]], data[[y_var]]) #this is the method we learned in class, using sklearn to model the linear regression
plt.plot(data[[x_var]], model.predict(data[[x_var]]), color='k') #The line on the plot
plt.savefig("linear_regression_python_output.png")
rsquare = model.score(data[[x_var]], data[[y_var]]) #Outputs the R squared value
print("R Squared Equals:")
print(rsquare)
plt.show()



# In[ ]:




