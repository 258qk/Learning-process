import torch
import matplotlib.pyplot as plt

# requires_grad=True → 打开"操作录音"（只记录，不计算）
x = torch.tensor(3.0, requires_grad=True)
y = x ** 2

# .backward() → 倒着放录音，算出导数，填入 .grad
# ⚠️ 必须先调用 backward()，x.grad 才有值，否则是 None
y.backward()
print(x.grad)  # 6.0（dy/dx = 2x，x=3时斜率为6）

# ========== 练习 ==========

# 1. 换一个函数：y = 3x + 2，x=5，求梯度
# x1 = torch.tensor(5.0, requires_grad=True)
# y1 = 3 * x1 + 2
# y1.backward()
# print(f"练习1 — dy/dx = {x1.grad}")  # 3x+2的导数是3

# # 2. 多变量：y = x1² + x2³，求两个梯度
# x3 = torch.tensor(2.0, requires_grad=True)
# x4 = torch.tensor(3.0, requires_grad=True)
# y3 = x3**2 + x4**3
# y3.backward()
# print(f"练习2 — x3的梯度: {x3.grad}, x4的梯度: {x4.grad}")  # 4, 27

# # 3. 模拟"模型训练的一步"：参数 w=2.0，算梯度，沿梯度方向更新 w
# w = torch.tensor(2.0, requires_grad=True)
# loss = (w - 5)**2  # 假装"预测值"是 w，"目标值"是 5，loss 越小越好
# loss.backward()
# print(f"练习3 — 更新前 w={w.item():.2f}, 梯度={w.grad.item():.2f}")

# # 手动更新参数（把 w 往让 loss 变小的方向挪 0.1 步）
# with torch.no_grad():  # 更新时不需要追踪梯度
#     w -= 0.1 * w.grad
# print(f"练习3 — 更新后 w={w.item():.2f}")  # 应该从 2.0 更接近 5.0

##自检
# 题 1：算 y = 4x³，x=2 时的梯度
x_2 = torch.tensor(2.0, requires_grad=True)
y_2 = 4 * x_2**3
y_2.backward()
print(f"题目1: -dx/dy = {x_2.grad}")

# 题目2： 算 y = x₁² + 3x₂²，x₁=2, x₂=3 时两个变量的梯度
m1 = torch.tensor(2.0, requires_grad=True)
m2 = torch.tensor(3.0, requires_grad=True)
y_m = m1**2 + 3*m2**2
y_m.backward()
print(f"题目2: -dx₁/dy = {m1.grad}, -dx₂/dy = {m2.grad}")

# 题 3：模拟参数更新，从 w=10 开始，走 2 步
data_grad = []
w = torch.tensor(10.0, requires_grad=True)
step = 0
while abs(w.item() - 0) > 0.01:
    lose = (w - 0)**2
    lose.backward()
    with torch.no_grad():
        w -= 0.1 * w.grad
        data_grad.append(w.grad.item())
        w.grad.zero_()
        step += 1
        print(f"第 {step} 步更新 w={w.item():.2f}")
print(f"总共 {step} 步, 最终 w={w.item():.4f}")
plt.figure(figsize = (10, 6))
plt.plot(data_grad)
plt.xlabel("step")
plt.ylabel("grad")
plt.title("grad and step")
plt.show()



