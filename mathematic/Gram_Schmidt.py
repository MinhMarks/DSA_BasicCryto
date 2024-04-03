# Thank to gemini and linear algebra 


import numpy as np

# Khởi tạo ma trận v
v = [
    np.array([4, 1, 3, -1]),
    np.array([2, 1, -3, 4]),
    np.array([1, 0, -2, 7]),
    np.array([6, 2, 9, -5]),
]

# Khởi tạo u và v1
u = [v[0]]
v1 = v[1:]

# Lặp qua các phần tử trong v1
for vi in v1:
    # Tính toán uij và mi
    mi = [np.dot(vi, uj) / np.dot(uj, uj) for uj in u]

    # Cập nhật u
    u += [vi - sum([mij * uj for (mij, uj) in zip(mi, u)])]

# In kết quả
print(round(u[3][1], 5))