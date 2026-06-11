import torch
import matplotlib.pyplot as plt

# 造数据：y = 3x + 2 + 噪声（模拟传感器读数）
x = torch.linspace(0, 10, 50)
y_true = 3 * x + 2 + torch.randn(50) * 2  # 加噪声模拟真实世界

# 初始化参数（先瞎猜：w=0, b=0）
w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)

# ⚠️ 训练循环：backward 必须在 loss 计算之后
for step in range(900):
    y_pred = w * x + b                     # 预测值
    loss = ((y_pred - y_true) ** 2).mean() # 均方误差（越小越好）
    loss.backward()                         # 同时算出 w.grad 和 b.grad
    
    # ⚠️ 先记录梯度再更新（否则清零后取不到）
    w_grad_val = w.grad.item()
    b_grad_val = b.grad.item()
    
    with torch.no_grad():
        w -= 0.01 * w.grad
        b -= 0.01 * b.grad
    
    w.grad.zero_()
    b.grad.zero_()
    
    # 前 5 步 + 每 20 步打印一次
    if step < 5 or step % 20 == 0:
        print(f"Step {step:3d} | loss={loss.item():7.2f} | "
              f"w={w.item():.4f} (grad={w_grad_val:+.2f}) | "
              f"b={b.item():.4f} (grad={b_grad_val:+.2f})")

print(f"\n训练结果: w = {w.item():.2f}, b = {b.item():.2f}")
print(f"正确答案: w = 3.00, b = 2.00")