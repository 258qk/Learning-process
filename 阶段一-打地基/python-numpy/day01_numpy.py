"""
Day 01: NumPy 入门 —— 三行业通用基础
无人机/通信/导航都需要的数据运算能力
"""

import numpy as np

data_1 = np.array([1,2,3,4,5]) #data_1 是 NumPy 数组
data_2 = [1,2,3,4,5] #data_2是 Python 列表
print("每个元素加10:", data_1 + 10) #此处不会报错，因为 ndarray 可以直接加法
 #print(data_2 + 10) # 此处会报错，因为 Python 列表不能直接加法
for i in data_2:
    data_2[i] += 10
# python列表只能使用循环遍历，不能直接加法
print("每个元素加10:", data_2)

print("平均值:", data_1.mean())
# 计算列表的平均值
vag = 0
for i in data_2:
    vag += data_2[i] 

vag /= len(data_2)
print("平均值:", vag)











# print("=" * 50)
# print("1. 创建数组 —— 相当于 C 里的数组，但能整批运算")
# print("=" * 50)

# # 和你在单片机上 int arr[] = {1,2,3,4,5} 类似
# data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print("原始数据:", data)
# print("全部 + 10:", data + 10)         # C 里要写 for 循环，这里不用
# print("全部 * 2:", data * 2)
# print("全部平方:", data ** 2)
# print("平均值:", data.mean())
# print("最大值:", data.max(), "| 最小值:", data.min())

# print()
# print("=" * 50)
# print("2. 矩阵运算 —— 无人机姿态 / 导航定位全靠它")
# print("=" * 50)

# # 2x2 矩阵（比如旋转矩阵、协方差矩阵）
# mat = np.array([[1, 2],
#                 [3, 4]])

# print("矩阵:\n", mat)
# print("矩阵转置:\n", mat.T)            # 行变列，列变行
# print("矩阵乘法 (mat @ mat):\n", mat @ mat)
# print("对应元素相乘 (mat * mat):\n", mat * mat)  # 注意：和矩阵乘不一样！

# # 实际例子：坐标旋转（比如无人机机体坐标转地面坐标）
# angle = np.radians(30)  # 30度转弧度
# rotation = np.array([[np.cos(angle), -np.sin(angle)],
#                      [np.sin(angle),  np.cos(angle)]])
# body_vector = np.array([1.0, 0.0])    # 机的 x 轴方向
# ground_vector = rotation @ body_vector # 转到地面坐标系
# print(f"\n30度旋转矩阵:\n{rotation}")
# print(f"机体向量 {body_vector} → 地面向量 {ground_vector}")

# print()
# print("=" * 50)
# print("3. 信号生成 —— 通信 / 导航天天见")
# print("=" * 50)

# # 生成 0~1 秒的 100 个采样点（相当于你的 ADC 采样）
# t = np.linspace(0, 1, 100)
# # 5Hz 正弦波
# signal = np.sin(2 * np.pi * 5 * t)
# print("时间点前5个:", t[:5])
# print("信号值前5个:", signal[:5])
# print(f"信号均值: {signal.mean():.4f}")
# print(f"信号最大幅度: {signal.max():.4f}")

# # 加噪声 —— 模拟真实信号
# noisy_signal = signal + np.random.normal(0, 0.1, 100)
# print(f"加噪后信号均值: {noisy_signal.mean():.4f}")

# print()
# print("=" * 50)
# print("Day 01 完成！核心收获：")
# print("  - 数组整批运算（不用写 for 循环）")
# print("  - 矩阵乘法和转置（无人机/导航坐标变换）")
# print("  - 信号生成和噪声（通信信号处理基础）")
# print("=" * 50)
