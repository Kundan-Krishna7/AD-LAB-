import matplotlib.pyplot as plt
from scipy import stats
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,6,8,10,12,14,16,18,20]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print("Regression Coefficients: ", slope, " and ", intercept)
print("p-value= ",p)
print("R2 Score= ",r)
print("Standard Error= ",std_err)
print("Equation of line:")
print("y=",round(slope,2),"x","+",round(intercept,2),"+",round(std_err,0))
print("For x=11, y=",myfunc(11))
import pandas as pd
df=pd.read_csv("Housing(1).csv",index_col=None)
print(df)
df.info()
import seaborn as sns
sns.heatmap(data=df.corr(numeric_only=True), annot=True, linecolor='white', linewidths=0.25)
y=df[['price']]
X=df[['area']]
y
X
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X,y,random_state=42,train_size=0.7)
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

reg = LinearRegression().fit(X_train, y_train)

print("Regression Coefficient=",reg.coef_)
print("Regression Intercept=",reg.intercept_)
print("Mean Absolute Error=",mean_absolute_error(y_train, reg.predict(X_train)))
print("Mean Squared Error=",mean_squared_error(y_train, reg.predict(X_train)))
print("Root Mean Squared Error=",np.sqrt(mean_squared_error(y_train, reg.predict(X_train))))
print("R2 Score=",reg.score(X_train, y_train))
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

X=[[1],[2],[3],[4],[5],[6],[7],[8]]
y=[14,22,24,32,36,41,44,52]
reg = LinearRegression().fit(X, y)

print("Actual Output=",y)
print("Predicted Output=",reg.predict(X))
print("Regression Coefficient=",reg.coef_)
print("Regression Intercept=",reg.intercept_)
print("Mean Absolute Error=",mean_absolute_error(y, reg.predict(X)))
print("Mean Squared Error=",mean_squared_error(y, reg.predict(X)))
print("Root Mean Squared Error=",np.sqrt(mean_squared_error(y, reg.predict(X))))
print("R2 Score=",reg.score(X, y))

plt.scatter(X, y,color='green')
plt.plot(X, reg.predict(X),color='red', marker='*')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Actual Output", "Predicted Output (Regression Line)"], loc="upper left")
plt.show()
import matplotlib.pyplot as plt

plt.scatter(X_train, y_train, color='black')
plt.plot(X_train, reg.predict(X_train), color='red')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Actual Output", "Predicted Output (Regression Line)"], loc="upper left")
plt.show()