#!/usr/bin/env python
# coding: utf-8

# # Linear Regression in Python

import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.stats import pearsonr
import numpy as np #these are all necessary packages for the graph and the line

if len(sys.argv) != 4:
    print("Enter file name, your x variable, and your y variable after the script name: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_var = sys.argv[2]
y_var = sys.argv[3]

# importing the dataset

data = pd.read_csv(filename) #re-reading the csv, using pandas to make it more malleable for data analysis


import csv #importing the csv file
with open(filename, 'r') as lr_data: #opening the csv file and renaming it
    csv_reader = csv.reader(lr_data) #reading the csv file
    for row in csv_reader:
        print(row) #for every single row of our CSV file, print it

x_lr = np.array(data[x_var]) #creating a variable out of an array of the x values in the CSV file
y_lr = np.array(data[y_var]) #creating a variable out of an array of the y values in the CSV file

plt.scatter(data[[x_var]], data[[y_var]], color='b') #creates the scatterplot of the data using matplotlib and the two created arrays for the data
plt.title(f'{y_var} vs {x_var}') #title of the plot
plt.xlabel(x_var) #the title of the x axis
plt.ylabel(y_var) #the title of the y axis
slope, intercept = np.polyfit(data[x_var], data[y_var], 1) #creating variables for slope and intercept using the numpy function
y_pred = slope * data[[x_var]] + intercept #creating the y_pred variable
from sklearn.linear_model import LinearRegression #grabbing the linearregresion module
model = LinearRegression()
model.fit(data[[x_var]], data[[y_var]]) #this is the method we learned in class, using sklearn to model the linear regression
plt.plot(data[[x_var]], model.predict(data[[x_var]]), label='Fitted Line') #The line on the plot
from sklearn.metrics import mean_squared_error #MSE module
mse = mean_squared_error(data[[y_var]], y_pred) #MSE calculation
r2_value = model.score(data[[x_var]], data[[y_var]]) #calculated the rsquared value
corrcoef = np.corrcoef(x_lr, y_lr)[0,1] #calculating the r value using the arrays created up there, not used in further data
correlation, p_value = pearsonr(x_lr, y_lr) #creating the correlation coefficient and a p-value. p value is not used.
plt.figtext(0.15, 0.83, f'y = {slope:.2f}x + {intercept:.2f}') #labeling the figure
plt.figtext(0.15, 0.77, f'r = {correlation:.2f}')
plt.figtext(0.15, 0.72, f'MSE = {mse:.2f}')
plt.figtext(0.15, 0.67, f'r^2 = {r2_value:.2f}')
plt.legend(loc='lower right') #placing the legend in the lower right to avoid the stat analysis
plt.savefig("linear_regression_python_output.png") #saving the figure
plt.show()






