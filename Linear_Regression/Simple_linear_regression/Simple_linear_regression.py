# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 18:42:04 2020

@author: Acer
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#creating working directory and read data

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[: ,:-1].values
y=dataset.iloc[: , 1].values

#spliting of data 


from sklearn.model_selection import train_test_split 
X_train ,X_test ,y_train ,y_test = train_test_split(X,y, test_size=1/3 ,random_state = 0)

#fiting linear simple regression to te training data
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train, y_train)

#predicting test result
y_pred = regressor.predict(X_test)

#Visualization of training set 

plt.scatter(X_train, y_train, color='red')
plt.plot(X_train , regressor.predict(X_train),color='blue')
plt.title('Salary vs Experession(Training set)')
plt.xlabel('Experience')
plt.ylabel('salary')
plt.show()

"""#Visualization of test set 
plt.scatter(X_test, y_test, color='red')
plt.plot(X_test , regressor.predict(X_test),color='blue')
plt.title('Salary vs Experession(Test set)')
plt.xlabel('Experience')
plt.ylabel('salary')
plt.show()
"""