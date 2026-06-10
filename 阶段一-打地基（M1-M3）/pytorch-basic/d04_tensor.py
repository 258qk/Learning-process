"""
Day 04: Tensor 操作
2026.6.10
"""
import torch
import numpy as np

# 练1：把传感器数据转成 Tensor
np_data = np.random.randn(100, 4)   # 模拟 100 采样点 x 4 通道
tensor_data = torch.tensor(np_data)
print("Tensor shape:", tensor_data.shape)
print("第2行第3列:\n", tensor_data[1:3,:3])

# 练2：Tensor 运算 = NumPy 运算
print("\n均值:", tensor_data.mean())
print("每列均值:", tensor_data.mean(dim=0))  # dim=0 就是 NumPy 的 axis=0

# 练3：Tensor ↔ NumPy 互转
np_data_back = tensor_data.numpy()
print("\n转回 NumPy 类型:", type(np_data_back))

#自检
#生成采样点
new_np_data= np.random.randn(100,2)
new_tensor_data = torch.tensor(new_np_data)
print("均值：",new_tensor_data.mean())
print("每列均值：",new_tensor_data.mean(dim=0))
print("新 tensor shape:", new_tensor_data.shape)
print("第2行到第4行,第1到第2列:\n", new_tensor_data[1:4,:2])
