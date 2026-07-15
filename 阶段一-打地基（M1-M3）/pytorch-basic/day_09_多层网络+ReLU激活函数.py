import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# ---------- 造抛物线数据 ----------
x = torch.linspace(-5, 5, 100).unsqueeze(1)  # (100,1)
y = x ** 2                                     # y = x²

# ---------- 两层 Linear，不加激活 ----------
model_relu = nn.Sequential(
    nn.Linear(1, 8),
    nn.ReLU(),
    nn.Linear(8, 1)
)

# ---------- 训练 ----------
optimizer = torch.optim.SGD(model_relu.parameters(), lr=0.001)
for epoch in range(12000):
    y_pred = model_relu(x)
    loss = ((y_pred - y) ** 2).mean()
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

# ---------- 画图 ----------
with torch.no_grad():
    y_pred = model_relu(x)

plt.figure(figsize=(6, 4))
plt.scatter(x, y, s=2, label = 'x²')
plt.plot(x, y_pred, 'r-', label='预测（加ReLU）')   
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('两层Linear叠起来 = 还是一根直线')
plt.show()
print(f"损失: {loss.item():.4f}")

# 看看 Linear 内部是不是矩阵乘法
h = x @ model_relu[0].weight.T + model_relu[0].bias
h_relu = torch.relu(h)
y_manual = h_relu @ model_relu[2].weight.T + model_relu[2].bias
print("手写矩阵乘法结果:", y_manual[:3].T)
print("model(x) 结果:", model_relu(x)[:3].T)