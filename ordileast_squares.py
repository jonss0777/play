from sklearn import linear_model
reg = linear_model.LinearRegression()

reg.fit([[1,1], [2,2], [3,3],  [4,4]], [1,2,3,4])

print(reg.coef_)