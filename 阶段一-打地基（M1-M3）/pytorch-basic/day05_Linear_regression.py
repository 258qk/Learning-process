import torch
import numpy as np
import matplotlib.pyplot as plt
import os   

script_dir = os.path.dirname(os.path.abspath(__file__))

# data_w = [0] * 900 #记录w的梯度
# data_b = [0] * 900 #记录b的梯度
# w_value = [] #记录w的值
# b_value = [] #记录b的值
# # 造数据：y = 3x + 2 + 噪声（模拟传感器读数）
# x = torch.linspace(0, 10, 50)
# y_true = 3 * x + 2 + torch.randn(50) * 2  # 加噪声模拟真实世界
# # 初始化参数（先瞎猜：w=0, b=0）
# w = torch.tensor(0.0, requires_grad=True)
# b = torch.tensor(0.0, requires_grad=True)

# # ⚠️ 训练循环：backward 必须在 loss 计算之后
# for step in range(900): 
#     y_pred = w * x + b                     # 预测值
#     loss = ((y_pred - y_true) ** 2).mean() # 均方误差（越小越好）
#     loss.backward()                         # 同时算出 w.grad 和 b.grad
    
#     # ⚠️ 先记录梯度再更新（否则清零后取不到）
#     w_grad_val = w.grad.item()
#     b_grad_val = b.grad.item()
#     data_w[step] = w_grad_val
#     data_b[step] = b_grad_val
#     with torch.no_grad():
#         w -= 0.01 * w.grad
#         b -= 0.01 * b.grad
#     if step % 30 == 0:                      # ⚠️ 每 30 步存一条线
#         w_value.append(w.item())
#         b_value.append(b.item())
#     w.grad.zero_()
#     b.grad.zero_()

# print(f"\n训练结果: w = {w.item():.2f}, b = {b.item():.2f}")
# print(f"正确答案: w = 3.00, b = 2.00")
# # 画图
# plt.figure(figsize = (10, 6))
# plt.scatter(x.numpy(), y_true.numpy(), alpha=0.5, s=10,label = "true")
# for i in range(len(w_value)):
#     w_val = w_value[i]
#     b_val = b_value[i]
#     alpha = 0.1 + 0.9 * (i / len(w_value))
#     if i == len(w_value) - 1:
#         color = "red"
#         label = f"最终拟合: y={w_val:.2f}x+{b_val:.2f}"
#     else:
#         color = "blue"
#         label = None
#     plt.plot(x.numpy(), (w_val * x.numpy() + b_val), 
#              alpha=alpha, color=color, label=label)
# plt.legend()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Linear Regression")
# plt.savefig(os.path.join(script_dir, "linear_regression.png"))
# plt.show()


# 自检：
# 造数据 ： 
x = torch.linspace(0,10,50)  # 50个点，从0到10
y_ture = 3*x**2+ 4 + torch.randn(50) *2  # 50个点，加噪声模拟真实世界
timeout = 0 # 超时时间
# 初始化参数（先瞎猜：w=0, b=0）
w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)
# 画图
plt.figure(figsize = (10, 6))
# 数据存储
w_value = []
b_value = []
loss = torch.tensor(float('inf'))  # 初始设为无穷大，确保进入循环

while loss.item() > 0.01:
    timeout += 1
    y_pred = w * x**2 + b
    loss = ((y_pred - y_ture) ** 2).mean()
    loss.backward()
    w_value.append(w.item())
    b_value.append(b.item())
    with torch.no_grad():
        w -= 0.01 * w.grad
        b -= 0.01 * b.grad
    w.grad.zero_()
    b.grad.zero_()
    if timeout > 2000:
        print("训练超时")
        print("w = ", w.item())
        print("b = ", b.item())
        break
plt.scatter(x.numpy(), y_ture.numpy(), alpha=0.5, s=10,label = "true")
for i in range(len(w_value)):
    w_val = w_value[i]
    b_val = b_value[i]
    alpha = 0.1 + 0.9 * (i / len(w_value))
    if i == len(w_value) - 1:
        color = "red"
        label = f"最终拟合: y={w_val:.2f}x^2+{b_val:.2f}"
    else:
        color = "blue"
        label = None
    plt.plot(x.numpy(), (w_val * x.numpy() ** 2 + b_val), 
             alpha=alpha, color=color, label=label)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression")
plt.savefig(os.path.join(script_dir, "linear_regression.png"))
plt.show()