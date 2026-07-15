import torch
import os
import torch.nn as nn
import numpy as np
from torch.utils.data import TensorDataset, DataLoader, random_split
#---------生成数据---------------

script_dir = os.path.dirname(os.path.abspath(__file__))

hour = 24 * 30
np.random.seed(42)

t = np.arange(0, hour, 1.0)

daily_cycle = 15 + 10 * np.sin(2 * np.pi * t / 24 + np.pi/2)

trend = 0.05 * t

noise = np.random.randn(hour) * 1.5

my_temp = daily_cycle + trend + noise
print(f"生成温度数据形状: {my_temp.shape}")
np.savetxt(os.path.join(script_dir, "my_temperature_data.csv"),
           my_temp.reshape(-1, 1),
           delimiter=",",
           header="temperature",
           comments="")
print(f"生成温度数据 {len(my_temp)} 条")
print(f"温度范围：{my_temp.min():.1f}°C ~ {my_temp.max():.1f}°C")

#---------读取数据---------------

my_temp = np.loadtxt(os.path.join(script_dir, "my_temperature_data.csv"), delimiter=",", skiprows=1)
print(f"读取温度数据 {len(my_temp)} 条")

#---------滑窗切样本---------------

seq_len = 24
X = []
y = []
# 滑窗切样本：前24小时预测下一小时
for i in range(len(my_temp) - seq_len):
    X.append(my_temp[i:i+seq_len])
    y.append(my_temp[i+seq_len])

X = np.array(X, dtype=np.float32)
y = np.array(y, dtype=np.float32)
X_tensor = torch.from_numpy(X)
y_tensor = torch.from_numpy(y).unsqueeze(1)
print(X_tensor.shape)
print(y_tensor.shape)

#---------切分训练/测试---------------
train_size = int(0.8 * len(X_tensor))
test_size = len(X_tensor) - train_size
train_dataset, test_dataset = random_split(TensorDataset(X_tensor, y_tensor), [train_size, test_size])
print(f"训练集: {len(train_dataset)}, 测试集: {len(test_dataset)}")

#---------DataLoader---------------
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
test_loader  = DataLoader(test_dataset, batch_size=32)
print(f"分组训练集: {len(train_loader)}, 分组测试集: {len(test_loader)}")

#---------模型---------------
model = nn.Sequential(
    nn.Linear(24, 16),
    nn.ReLU(),
    nn.Linear(16, 1)
)
optimizer = torch.optim.Adam(model.parameters(), lr = 0.001,weight_decay=0.1)

for epoch in range(1000):
    model.train()
    for batch_x, batch_y in train_loader:
        y_pred = model(batch_x)
        loss = ((y_pred - batch_y) ** 2).mean()
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
    
    model.eval()
    with torch.no_grad():
        train_idx = train_dataset.indices
        test_idx = test_dataset.indices
        train_loss = ((model(X_tensor[train_idx]) - y_tensor[train_idx]) ** 2).mean().item()
        test_loss  = ((model(X_tensor[test_idx])  - y_tensor[test_idx])  ** 2).mean().item()
    
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Train Loss: {train_loss:.4f}, Test Loss: {test_loss:.4f}")

torch.save(model.state_dict(), os.path.join(script_dir, "my_temp_model.pth"))
print(f"\n训练完成，最终train_loss={train_loss:.4f}，test_loss={test_loss:.4f}")
print(f"模型已保存：my_temp_model.pth")

