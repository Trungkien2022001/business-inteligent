import numpy as np
from sklearn.linear_model import LinearRegression

# Dữ liệu doanh số của 12 tháng đầu
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # Tháng
y = np.array([1822256, 2202022,2807100,3390670,3152606,2577802,2647775,2244467,2097560,3736726,3199603,4613443])  # Doanh thu
y1 = np.array([10903, 13449, 17005, 20558, 18667, 15253, 16072, 13448, 13109, 22703, 19798, 28114])  # Doanh số

# Tạo mô hình hồi quy tuyến tính
model = LinearRegression()
model1 = LinearRegression()
model.fit(x.reshape(-1, 1), y)
model1.fit(x.reshape(-1, 1), y1)

# Dự đoán doanh số tháng 13
predicted_sales = model.predict([[13]])
predicted_sales1 = model1.predict([[13]])

print('hồi quy tuyến tính, doanh thu: ',int(round(predicted_sales[0])), '$, doanh số: ', int(round(predicted_sales1[0])))

from sklearn.naive_bayes import GaussianNB
# Tạo mô hình hồi quy tuyến tính
model = GaussianNB()
model1 = GaussianNB()
model.fit(x.reshape(-1, 1), y)
model1.fit(x.reshape(-1, 1), y1)

# Dự đoán doanh số tháng 13
predicted_sales = model.predict([[13]])
predicted_sales1 = model1.predict([[13]])

print('Naive bayes, doanh thu: ',int(round(predicted_sales[0])), '$, doanh số: ', int(round(predicted_sales1[0])))

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model1 = RandomForestRegressor()
model.fit(x.reshape(-1, 1), y)
model1.fit(x.reshape(-1, 1), y1)

# Dự đoán doanh số tháng 13
predicted_sales = model.predict([[13]])
predicted_sales1 = model1.predict([[13]])

print('Random Forest, doanh thu: ',int(round(predicted_sales[0])), '$, doanh số: ', int(round(predicted_sales1[0])))

from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor()
model1 = GradientBoostingRegressor()
model.fit(x.reshape(-1, 1), y)
model1.fit(x.reshape(-1, 1), y1)

# Dự đoán doanh số tháng 13
predicted_sales = model.predict([[13]])
predicted_sales1 = model1.predict([[13]])

print('Hồi quy Gradient Boosting, doanh thu: ',int(round(predicted_sales[0])), '$, doanh số: ', int(round(predicted_sales1[0])))

from sklearn.svm import SVR
model = SVR()
model1 = SVR()
model.fit(x.reshape(-1, 1), y)
model1.fit(x.reshape(-1, 1), y1)

# Dự đoán doanh số tháng 13
predicted_sales = model.predict([[13]])
predicted_sales1 = model1.predict([[13]])

# print('SVR, doanh thu: ',int(round(predicted_sales[0])), '$, doanh số: ', int(round(predicted_sales1[0])))
# from sklearn.neural_network import MLPRegressor
# model = MLPRegressor()
# model1 = MLPRegressor()
# model.fit(x.reshape(-1, 1), y)
# model1.fit(x.reshape(-1, 1), y1)

# # Dự đoán doanh số tháng 13
# predicted_sales = model.predict([[13]])
# predicted_sales1 = model1.predict([[13]])

# print('MLPRegressor, doanh thu: ',int(round(predicted_sales[0])), '$, doanh số: ', int(round(predicted_sales1[0])))
