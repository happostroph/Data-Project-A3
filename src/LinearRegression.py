import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #lib name : scikit-learn

#import LinearRegression.csv
#importe LinearRegression.csv
data = pd.read_csv('/Data-Project-A3/Datas/linearRegression.csv', index_col=0)
data.head()

#Create the object Linear regression
#créer un objet reg lin
modeleReg=LinearRegression()

#Create y and X
#créer y et X
axes=data.columns.drop("time")
y=data.time
X=data[axes]

modeleReg.fit(X,y)

print(modeleReg.intercept_)
print(modeleReg.coef_)

#Calculate R²
#calcul du R²
modeleReg.score(X,y)

RMSE=np.sqrt(((y-modeleReg.predict(X))**2).sum()/len(y))

plt.plot(y, modeleReg.predict(X),'.')
plt.show()

plt.plot(y, y-modeleReg.predict(X),'.')
plt.show()

#TODO add the y=aX+b formule and a prompt to predict