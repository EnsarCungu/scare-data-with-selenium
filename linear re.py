import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("C:\\Users\\hh\\Desktop\\projekti_1\\Banesat.csv")

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1:].values

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 2/3, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

plt.scatter(x_train, y_train, color="red")
plt.plot(x_train, regressor.predict(x_train), color="blue")
plt.title("Cmimi i shtepijave ne baze te m2")
plt.xlabel("Metri Katror")
plt.ylabel("Cmimi")
plt.show()


plt.scatter(x_test, y_test, color="red")
plt.scatter(x_test, regressor.predict(x_test), color="green")
plt.plot(x_train, regressor.predict(x_train), color="blue")
plt.title("Cmimi i shtepijave ne baze te m2")
plt.xlabel("Metri Katror")
plt.ylabel("Cmimi")
plt.show()
