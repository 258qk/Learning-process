import torch
import torch.nn as nn
import numpy as np
import os
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))

# ========== 1. 读数据 + 滑窗（和训练时一样） ==========
temp = np.loadtxt(os.path.join(script_dir, "my_temperature_data.csv"),
                  delimiter=",", skiprows=1)
print(f"读取温度数据 {len(temp)} 条")

seq_len = 24
X, y = [], []
for i in range(len(temp) - seq_len):
    X.append(temp[i:i+seq_len])
    y.append(temp[i+seq_len])

X = np.array(X, dtype=np.float32)
y = np.array(y, dtype=np.float32)
X_tensor = torch.from_numpy(X)
y_tensor = torch.from_numpy(y).unsqueeze(1)
print(f"共 {len(X)} 组样本")

# ========== 2. 加载训练好的模型 ==========
model = nn.Sequential(
    nn.Linear(24, 16),
    nn.ReLU(),
    nn.Linear(16, 1)
)
model.load_state_dict(torch.load(os.path.join(script_dir, "my_temp_model.pth")))
model.eval()

# ========== 3. 全量预测 ==========
with torch.no_grad():
    y_pred = model(X_tensor).squeeze().numpy()

# ========== 4. 画图 ==========
plt.figure(figsize=(12, 4))

# 子图1：完整时间序列
plt.subplot(1, 2, 1)
t = np.arange(len(y))
plt.plot(t, y, 'b-', linewidth=1.5, label='真实值')
plt.plot(t, y_pred, 'r--', linewidth=1.5, label='预测值')
plt.xlabel('时间（小时）')
plt.ylabel('温度（°C）')
plt.title('温度预测 — 完整序列')
plt.legend()
plt.grid(True)

# 子图2：放大最后 100 小时
plt.subplot(1, 2, 2)
t_zoom = t[-100:]
plt.plot(t_zoom, y[-100:], 'b-o', markersize=3, linewidth=1, label='真实值')
plt.plot(t_zoom, y_pred[-100:], 'r-s', markersize=3, linewidth=1, label='预测值')
plt.xlabel('时间（小时）')
plt.ylabel('温度（°C）')
plt.title('温度预测 — 最后 100 小时')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# ========== 5. 误差指标 ==========
mse = ((y_pred - y) ** 2).mean()
mae = np.abs(y_pred - y).mean()
print(f"MSE={mse:.4f}, MAE={mae:.4f}（平均误差 ±{mae:.1f}°C）")
