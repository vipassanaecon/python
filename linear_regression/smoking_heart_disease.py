#import packages
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#extract data and create dataframe
df = pd.read_csv(r"heart_disease.data.csv", delimiter=",", encoding= 'unicode_escape')
df

#assign independent and dependent variables
#The reshape function converts our one dimensional array 
#into a two-dimensional array with as many rows as possible (-1) with one column (1). 
#This is required in order to do the regression analysis. 
#Our dependent variable, heart_disease, can remain a one dimensional array.

smoking = df.values[:, 1].reshape((-1, 1)) #all rows of 2nd column (index 1) of file (reshap
heart_disease = df.values[:, 2] #all rows of 3rd column (index 2) of file 

#.fit is used to calculate the estimators of the model, 
# or the optimal weights of b₀ (our intercept) and b₁(our slope)
# and find the best “fitted” line to our data points.
fit = LinearRegression().fit(smoking, heart_disease)

#get stats
r_squared = fit.score(smoking, heart_disease)
print('coefficient of determination:', r_squared)

print('intercept:', fit.intercept_) 
print('slope:', fit.coef_) 

#visualize model
plt.figure(figsize=(9,7))
plt.plot(smoking, heart_disease, 'o') #scatterplot
plt.plot(smoking, fit.predict(smoking), color = "black")
plt.title("smoking and heart disease")
plt.xlabel("smoking")
plt.ylabel("heart disease")
plt.axis([0, 32, 0, 22])
plt.show()
