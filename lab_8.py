import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


bh_data = load_boston()
boston = pd.DataFrame(bh_data.data, columns=bh_data.feature_names)
print(boston.columns)
boston['MEDV'] = bh_data.target
A = boston.drop('MEDV', axis=1)
B = boston['MEDV']
A_train, A_test, B_train, B_test = train_test_split(A, B, test_size = 0.2, random_state=9)


model=LinearRegression().fit(A_train,B_train)

p=model.predict(A_test)

MSE_1 = mean_squared_error(B_test, p)
r2_score_1= r2_score(B_test,p)
print("Mean squared error :",MSE_1)
print("R2 score : ",r2_score_1)

nulls = pd.DataFrame(boston.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)


boston = boston.select_dtypes(include=[np.number]).interpolate().dropna()


numeric_features = boston.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print (corr['MEDV'].sort_values(ascending=False)[1:4], '\n')


boston=boston.drop(columns=['PTRATIO', 'TAX', 'RAD', 'DIS', 'AGE', 'NOX', 'CHAS', 'INDUS', 'CRIM'],axis=1)
print(boston.columns)


X = boston.drop('MEDV', axis=1)
y = boston['MEDV']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=9)



model=LinearRegression().fit(X_train,y_train)


predict=model.predict(X_test)


MSE = mean_squared_error(y_test, predict)
r2_score = r2_score(y_test,predict)
print("Mean squared error :",MSE)
print("R2 score : ",r2_score)
