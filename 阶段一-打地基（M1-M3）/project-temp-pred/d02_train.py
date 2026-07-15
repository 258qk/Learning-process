import numpy as np
import os
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader, random_split

script_dir = os.path.dirname(os.path.abspath(__file__))

# ========== 1. 读取数据 ==========
temp = np.loadtxt(os.path.join(script_dir, "temperature_data.csv"),
                  delimiter=",", skiprows=1)
print(f"读取温度数据 {len(temp)} 条")

# ========== 2. 滑窗切样本：前24小时预测下一小时 ==========
seq_len = 24
X, y = [], []

for i in range(len(temp) - seq_len):
    X.append(temp[i:i+seq_len])
    y.append(temp[i+seq_len])

X = np.array(X, dtype=np.float32)
y = np.array(y, dtype=np.float32).reshape(-1, 1)
print(f"切出样本: {len(X)} 组, 每组输入 {seq_len} 个温度")

# ========== 3. 转 Tensor + 切分训练/测试 ==========
X_tensor = torch.from_numpy(X)
y_tensor = torch.from_numpy(y)

dataset = TensorDataset(X_tensor, y_tensor)
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size

train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
print(f"训练集: {len(train_dataset)}, 测试集: {len(test_dataset)}")

# ========== 4. DataLoader ==========
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
test_loader  = DataLoader(test_dataset, batch_size=32)

# ========== 5. 模型：24 → 64 → 1 ==========
model = nn.Sequential(
    nn.Linear(24, 64),
    nn.ReLU(),
    nn.Linear(64, 1)
)

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# ========== 6. 训练 ==========
train_losses, test_losses = [], []

for epoch in range(500):
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

    train_losses.append(train_loss)
    test_losses.append(test_loss)

    if epoch % 100 == 0:
        print(f"Epoch {epoch:3d}: train_loss={train_loss:.4f}, test_loss={test_loss:.4f}")

# ========== 7. 保存模型 ==========
torch.save(model.state_dict(), os.path.join(script_dir, "temp_model.pth"))
print(f"\n训练完成，最终 test_loss={test_losses[-1]:.4f}")
print(f"模型已保存：temp_model.pth")
