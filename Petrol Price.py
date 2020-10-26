# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:42:29 2020

@author: Trinayan Borah
"""

import pandas as pd
import pickle

dataset = pd.read_csv('petrol.csv')

X = dataset[['Delhi', 'Kolkata', 'Mumbai']]
y = dataset['Chennai']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

pickle.dump(regressor,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))