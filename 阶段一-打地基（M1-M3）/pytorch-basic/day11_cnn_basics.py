import numpy as np

# 6×6 灰度图（模拟）
image = np.array([
    [3, 0, 1, 5, 0, 2],
    [2, 6, 2, 4, 3, 1],
    [2, 4, 1, 0, 6, 2],
    [5, 6, 3, 2, 5, 3],
    [3, 1, 2, 5, 2, 4],
    [1, 5, 3, 1, 6, 2]
])

# 3×3 卷积核（边缘检测器——找竖线）
kernel = np.array([
    [-1,  0,  1],
    [-1,  0,  1],
    [-1,  0,  1]
])
# 手写卷积：核在原图上滑动
H, W = image.shape
K = kernel.shape[0]
out = np.zeros((H - K + 1, W - K + 1))   # 输出尺寸: (4, 4)

for i in range(out.shape[0]):
    for j in range(out.shape[1]):
        region = image[i:i+K, j:j+K]       # 取 3×3 窗口
        out[i, j] = (region * kernel).sum() # 逐元素乘加

print("原图:\n", image)
print("\n卷积核:\n", kernel)
print("\n输出特征图:\n", out)

# ============================================
# MaxPooling：2×2 窗口，取最大值
# ============================================
feature = np.array([
    [3, 1, 5, 2],
    [2, 8, 1, 4],
    [6, 2, 3, 1],
    [1, 5, 2, 7]
])

pool_size = 2
out_pool = np.zeros((2, 2))

for i in range(2):
    
    for j in range(2):
        region = feature[i*2:i*2+2, j*2:j*2+2]
        out_pool[i, j] = region.max()

print("\n原始特征图 (4×4):\n", feature)
print("\nMaxPooling (2×2核, 步长2) 输出 (2×2):\n", out_pool)