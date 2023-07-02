from sklearn.linear_model import LinearRegression
import numpy as np

# X là số sản phẩm bán ra của 12 tháng trước đó
X = [[10903], [13449], [17005], [20558], [18667], [15253], [16072], [13448], [13109], [22703], [19798], [28114]]
s=0
for i in X:
    s+=i[0]
s=int(round(s/12))
print(s)
# y là doanh thu tương ứng
y = [1822256, 2202022,2807100,3390670,3152606,2577802,2647775,2244467,2097560,3736726,3199603,4613443]
# for i in y:
    # print(i)
# Khởi tạo mô hình
model = LinearRegression()



# Huấn luyện mô hình
model.fit(X, y)
predicted_revenue = model.predict(np.array([28114]).reshape(1, -1))
print("Dự đoán doanh thu của tháng sau:", int(round(predicted_revenue[0])))
