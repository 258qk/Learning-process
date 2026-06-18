# import torch
# import torch.nn as nn

# model = nn.Linear(1, 1)              # 一行替代 w 和 b
# print(f"w = {model.weight.item():.4f}, b = {model.bias.item():.4f}")
# print(list(model.parameters()))       # 所有可训练参数

#  # # 造数据
# x = torch.linspace(0, 10, 100).unsqueeze(1)
# y = 3 * x + 2 + torch.randn(100, 1) * 2

# model = nn.Linear(1, 1)
# optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# for epoch in range(50):
#      y_pred = model(x)
#      loss = ((y_pred - y) ** 2).mean()
#      loss.backward()
#      optimizer.step()
#      optimizer.zero_grad()

# print(f"w = {model.weight.item():.2f}, b = {model.bias.item():.2f}")
# print(f"正确答案: w=3.00, b=2.00")# # 造数据
# x = torch.linspace(0, 10, 100).unsqueeze(1)
# y = 3 * x + 2 + torch.randn(100, 1) * 2


import torch
import torch.nn as nn
import matplotlib.pyplot as plt

x = torch.linspace(0,10,100).unsqueeze(1)
y = 3 * x + 2 + torch.randn(100,1)*2
w_value = []
b_value = []
y_pred_value = []
model = nn.Linear(1, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 初始化 loss 为一个大值，确保进入循环
loss = torch.tensor(float('inf'))

for epoch in range(200):
    y_pred = model(x)
    loss = ((y_pred - y)**2).mean()
    loss.backward()
    optimizer.step()
    w_value.append(model.weight.item())
    b_value.append(model.bias.item())
    optimizer.zero_grad()

print(f"拟合值——w = {model.weight.item():.2f}, b = {model.bias.item():.2f}")
print(f"正确答案: w=3.00, b=2.00")
