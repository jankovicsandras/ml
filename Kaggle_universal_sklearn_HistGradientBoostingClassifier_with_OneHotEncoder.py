# Universal Kaggle competition solver
#
# sklearn HistGradientBoostingClassifier with OneHotEncoder
# can be used to give a baseline score
#
# https://scikit-learn.org/1.2/modules/ensemble.html#histogram-based-gradient-boosting
# https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html#gradient-boosting-estimator-with-one-hot-encoding
#
# Competition name, Public Score, Comment
# Titanic - Machine Learning from Disaster, 0.77751
# Multi-Class Prediction of Obesity Risk, 0.90137
# Spaceship Titanic, 0.79448
# House Prices - Advanced Regression Techniques, 0.35336, TODO: why so bad result
# Santander Customer Transaction Prediction, 0.50898, train.csv was downsampled by approx. 1/50; every target is zero; TODO: why so bad result
# 
# Usage:
# 1. Run the default notebook template to get the file paths to train.csv and test.csv
# 2. Read the competition details carefully to get the names of the ID and Target columns
# 3. Edit the parameters, run, and manually remove the last empty line from output.csv
# 4. Submit output.csv

import numpy as np
import pandas as pd 
import sklearn
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.pipeline import make_pipeline
print(sklearn.__version__) # Kaggle has 1.2.2 as of 2024-02-29, this notebook works with this version

# Parameters, TODO: edit these according to the competition
trainfilename = '/kaggle/input/titanic/train.csv'
testfilename = '/kaggle/input/titanic/test.csv'
targetlabel = 'Survived'
idlabel = 'PassengerId'

# Pandas CSV load and split to features and target
dftrain = pd.read_csv(trainfilename)
dftest = pd.read_csv(testfilename)
features = dftrain.drop(targetlabel, axis=1)
target = dftrain[targetlabel]

# Make model, train and predict
ohet = make_column_transformer( ( OneHotEncoder(sparse_output=False, handle_unknown="ignore"),
        make_column_selector(dtype_include="object"), ), remainder="passthrough",
)
model = make_pipeline( ohet, HistGradientBoostingClassifier(random_state=42) )
model.fit(features, target)
dftest[targetlabel] = model.predict(dftest)

# Save output
dftest.to_csv('output.csv', columns = [idlabel,targetlabel], index=False)
print('output.csv is saved.')
