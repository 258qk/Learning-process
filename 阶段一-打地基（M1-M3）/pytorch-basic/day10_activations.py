import torch
import matplotlib.pyplot as plt
# # ============================================
# # 1. 搭建你定义的网络：5输入 → 3隐藏 → 2输出
# # ============================================
# torch.manual_seed(42)

# # 输入（5个值）
# x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# # 第一层 Linear：5→3
# w1 = torch.tensor([[0.1, 0.2, 0.3, 0.4, 0.5],
#                    [0.2, 0.3, 0.1, 0.5, 0.4],
#                    [0.3, 0.1, 0.2, 0.4, 0.5]], requires_grad=True)
# b1 = torch.tensor([0.1, 0.2, 0.3], requires_grad=True)

# # 第二层 Linear：3→2
# w2 = torch.tensor([[0.5, 0.3, 0.2],
#                    [0.4, 0.5, 0.1]], requires_grad=True)
# b2 = torch.tensor([0.5, -0.5], requires_grad=True)

# # ============================================
# # 2. 前向传播
# # ============================================
# z = w1 @ x + b1          # [3,]   ← Linear1 算加权和
# a = torch.relu(z)        # [3,]   ← 激活函数：砍掉负数
# y = w2 @ a + b2          # [2,]   ← Linear2 算最终输出

# # 目标值（假设正确答案是 [1.0, -1.0]）
# target = torch.tensor([1.0, -1.0])
# loss = ((y - target) ** 2).sum() / 2   # MSE / 2（方便求导）

# print("=== 前向传播 ===")
# print(f"输入 x:       {x}")
# print(f"z = w1·x + b1: {z}")
# print(f"a = ReLU(z):   {a}")
# print(f"y = w2·a + b2: {y}")
# print(f"目标 target:   {target}")
# print(f"loss:          {loss.item():.4f}")

# # ============================================
# # 3. 反向传播
# # ============================================
# loss.backward()

# print("\n=== 反向传播：梯度（Autograd 自动算） ===")
# print(f"∂loss/∂w2:\n{w2.grad}")   # y 对 w2 的依赖 → 经过 a
# print(f"∂loss/∂b2: {b2.grad}")     # y 对 b2 的依赖
# print(f"∂loss/∂w1:\n{w1.grad}")   # 经过 y→a→ReLU→z→x
# print(f"∂loss/∂b1: {b1.grad}")

# 同一个任务：拟合 y = sin(x) 曲线
# ============================================
torch.manual_seed(42)
x = torch.linspace(-3, 3, 200).unsqueeze(1)       # (200,1)
y_true = torch.sin(x) + 0.1 * torch.randn(200, 1) # 加噪声

# 两个完全相同结构的模型
model_sgd = torch.nn.Sequential(
    torch.nn.Linear(1, 32),
    torch.nn.ReLU(),
    torch.nn.Linear(32, 32),
    torch.nn.ReLU(),
    torch.nn.Linear(32, 1)
)

model_adam = torch.nn.Sequential(
    torch.nn.Linear(1, 32),
    torch.nn.ReLU(),
    torch.nn.Linear(32, 32),
    torch.nn.ReLU(),
    torch.nn.Linear(32, 1)
)

# ⚠️ 先复制权重，确保起点完全一样
model_adam.load_state_dict(model_sgd.state_dict())

loss_fn = torch.nn.MSELoss()
optim_sgd = torch.optim.SGD(model_sgd.parameters(), lr=0.01)
optim_adam = torch.optim.Adam(model_adam.parameters(), lr=0.01)

loss_sgd_list = []
loss_adam_list = []

for epoch in range(1000):
    # --- SGD 训练 ---
    y_pred = model_sgd(x)
    loss_sgd = loss_fn(y_pred, y_true)
    optim_sgd.zero_grad()
    loss_sgd.backward()
    optim_sgd.step()
    loss_sgd_list.append(loss_sgd.item())

    # --- Adam 训练 ---
    y_pred = model_adam(x)
    loss_adam = loss_fn(y_pred, y_true)
    optim_adam.zero_grad()
    loss_adam.backward()
    optim_adam.step()
    loss_adam_list.append(loss_adam.item())

# ============================================
# 可视化对比
# ============================================
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 左图：loss 曲线
axes[0].plot(loss_sgd_list, label='SGD', alpha=0.7)
axes[0].plot(loss_adam_list, label='Adam', alpha=0.7)
axes[0].set_yscale('log')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Loss (log scale)')
axes[0].set_title('SGD vs Adam — Loss收敛对比')
axes[0].legend()
axes[0].grid(True)

# 右图：拟合效果
axes[1].scatter(x, y_true, s=5, alpha=0.3, label='真实数据')
axes[1].plot(x, model_adam(x).detach(), 'r-', linewidth=2, label='Adam拟合')
axes[1].plot(x, model_sgd(x).detach(), 'b--', linewidth=2, label='SGD拟合')
axes[1].legend()
axes[1].set_title('拟合效果：Adam(红实线) vs SGD(蓝虚线)')
axes[1].grid(True)

plt.tight_layout()
plt.show()

print(f"SGD  最终 loss: {loss_sgd_list[-1]:.6f}")
print(f"Adam 最终 loss: {loss_adam_list[-1]:.6f}")
