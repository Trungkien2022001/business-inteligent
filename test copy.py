import matplotlib.pyplot as plt
import random

# Tạo dữ liệu ngẫu nhiên cho trục y
y_values = [
                 0.2, 0.4632079354171277,
  0.6669336792992516,  0.816452407436906,
  0.8235099234979448, 0.9475401118389557,
  0.9622443389837672, 0.9754608505466136,
  0.9986065033669032, 0.9986620226044587,
  0.9997544753522309, 0.9998474648326996,
  0.9998700672775067, 0.9998802439269574,
  0.9999661602489114, 0.9999677437748615
]
print(len(y_values))
# Tạo dữ liệu cho trục x từ 1 đến 1000
x_values = list(range(1, 17))

# Vẽ biểu đồ
plt.plot(x_values, y_values)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Biểu đồ thể hiện chất lượng trung bình nhân viên của công ty')
plt.show()
