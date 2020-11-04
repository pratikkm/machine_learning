# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:54:40 2020

@author: Acer
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#creating working directory and read data

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[: ,:-1].values
y=dataset.iloc[: , 4:].values

# categorical data not working

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
#Encode Country Column
labelencoder_X = LabelEncoder()
X[:,3] = labelencoder_X.fit_transform(X[:,3])
ct = ColumnTransformer([("State", OneHotEncoder(), [3])], remainder = 'passthrough')
X = ct.fit_transform(X)

# avoiding dummy variable trap
X=X[:,1:]

#spliting of data

from sklearn.model_selection import train_test_split 
X_train ,X_test ,y_train ,y_test = train_test_split(X,y, test_size=0.2 ,random_state = 0)

#fitting multiple linear regression data into training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train , y_train)

#predicting the test result
y_pred = regressor.predict(X_test)

#Building optiomal model using Backward elimination
import statsmodels.api as sm
X = np.append(arr=np.ones((50,1)).astype(int) ,values=X,axis=1)

X_optimal=X[:,[0,1,2,3,4,5]]
X_optimal = X_optimal.astype(np.float64)
regressor_OLS = sm.OLS(y, X_optimal).fit()
#regressor_OLS = sm.OLS(endog=y , exdog=X_optimal ).fit()
regressor_OLS.summary()

X_optimal=X[:,[0,1,3,4,5]]
X_optimal = X_optimal.astype(np.float64)
regressor_OLS = sm.OLS(y, X_optimal).fit()
#regressor_OLS = sm.OLS(endog=y , exdog=X_optimal ).fit()
regressor_OLS.summary()

X_optimal=X[:,[0,3,4,5]]
X_optimal = X_optimal.astype(np.float64)
regressor_OLS = sm.OLS(y, X_optimal).fit()
#regressor_OLS = sm.OLS(endog=y , exdog=X_optimal ).fit()
regressor_OLS.summary()

X_optimal=X[:,[0,3,5]]
X_optimal = X_optimal.astype(np.float64)
regressor_OLS = sm.OLS(y, X_optimal).fit()
#regressor_OLS = sm.OLS(endog=y , exdog=X_optimal ).fit()
regressor_OLS.summary()

X_optimal=X[:,[0,5]]
X_optimal = X_optimal.astype(np.float64)
regressor_OLS = sm.OLS(y, X_optimal).fit()
#regressor_OLS = sm.OLS(endog=y , exdog=X_optimal ).fit()
regressor_OLS.summary()



