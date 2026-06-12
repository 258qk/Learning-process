import torch
from torch.utils.data import TensorDataset, DataLoader

# 例子
# # 造 100 条数据：y = 3x + 2 + 噪声
# x = torch.linspace(0, 10, 100).unsqueeze(1)  # shape: (100, 1)
# y = 3 * x + 2 + torch.randn(100, 1) * 2      # shape: (100, 1)

# # 1️⃣ 打包成数据集（数据和标签放在一起）
# dataset = TensorDataset(x, y)

# # 2️⃣ 用 DataLoader 自动分批（每批 20 条，打乱顺序）
# loader = DataLoader(dataset, batch_size=20, shuffle=True)

# # 3️⃣ 跑一次看看每个 batch 长什么样
# for i, (batch_x, batch_y) in enumerate(loader):
#     print(f"Batch {i}: x shape={batch_x.shape}, y shape={batch_y.shape}")
#     print(f"  前 3 条 x: {batch_x[:3].squeeze().tolist()}")



# 造数据
x = torch.linspace(0, 10, 100).unsqueeze(1)   # ⚠️ x 不要太大，否则 x² 梯度爆炸
y_true = 3 * x**2 + 4 + torch.randn(100, 1) * 2
w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)
index = 0
w_grad_val = []
b_grad_val = []
w_val = []
b_val = []
# 打包成数据集（数据和标签放在一起）
dataset = TensorDataset(x, y_true)

# 用 Dataloader 打乱之后自动分批
loader = DataLoader(dataset ,batch_size = 20 ,shuffle = True)
for epoch in range(50):
    for i,(batch_x,batch_y) in enumerate(loader):
        y_pred = w * batch_x**2 +b
        lose = ((y_pred - batch_y) ** 2).mean()
        lose.backward()
        w_grad_val.append(w.grad.item())
        b_grad_val.append(b.grad.item())
        w_val.append(w.item())
        b_val.append(b.item())
        with torch.no_grad():
            w -= 0.0001 * w.grad       # ⚠️ 二次函数梯度大，学习率要极小
            b -= 0.005 * b.grad
        index += 1
        w.grad.zero_()
        b.grad.zero_()
print("训练完成")
print(f"w = {w.item():.2f}, b = {b.item():.2f}")
print(f"正确答案: w = 3.00, b = 4.00")
        



