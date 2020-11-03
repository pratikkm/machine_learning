# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:44:36 2020

@author: Acer
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#creating working directory and read data

dataset = pd.read_csv('Data.csv')
x = dataset.iloc[: ,:-1].values
y=dataset.iloc[: , 3:].values

# missing data in file 

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan ,strategy = 'mean')
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])

# categorical data not working

from sklearn.preprocessing import LabelEncoder , OneHotEncoder
from sklearn.compose import ColumnTransformer
#labelencoder_X= LabelEncoder()
#x[:,0]=labelencode_X.fit_transform(x[:,0])
#onehotencoder = OneHotEncoder(categorical_features=[0])
#x=onehotencoder.fit_transform(x).toarray()
#labelencode_Y = LabelEncoder()
#y=labelencoder_X.fit_transform(y)
ct_X = ColumnTransformer( transformers=[('encode',OneHotEncoder(),[0])],remainder='passthrough')
x=ct_X.fit_transform(x)
y=ct_X.fit_transform(y)

#spliting of data

from sklearn.model_selection import train_test_split 
X_train ,X_test ,Y_train ,Y_test = train_test_split(x,y, test_size=0.2 ,random_state = 0)

# scalling 

from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
Y_train = sc_y.fit_transform(y_train)




















