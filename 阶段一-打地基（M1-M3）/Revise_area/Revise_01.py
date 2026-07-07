import numpy as np
import torch as th
# # 第一组：NumPy 基础操作
# #1. 
# x = np.linspace(0,10,10) #linspace(start,stop,num)
# y = np.arange(0,10,10)  #arange(start,stop,step)

# #2. 
# a = np.ones((5,1))
# b = np.zeros((5,1))

# #3.
# c = np.random.randn(2,2)

# #4.
# d = np.array([[1,2,3,4],
#             [5,6,7,8]])

# #6.
# e = np.arange(1,10,1)

# #7.
# e_shape = e.shape

# 第二组：PyTorch Tensor + autograd（8 题）
# 1.
# x = th.tensor([1,2,3])  # 可以使用requires_grad=True来计算梯度的张量
# print(x)
# print(x.shape)
# x_new = x.unsqueeze(0)
# print(x_new)
# print(x_new.shape)

# 5.
# r = th.rand(2,3)
# print(type(r))
# p = r.numpy()
# print(type(p))
# q = th.from_numpy(p)
# print(type(q))

#6.
#requires_grad=True 的作用是对梯度变化进行记录追踪，如果不加的话就无法计算梯度
#loss.backward() 的作用是对计算进行反向传播，计算梯度
#w.grad.zero_()的作用是停止梯度计算，防止梯度累加


#第三组：训练框架

# 1.
x = th.linspace(0,10,100).unsqueeze(1)
y = 3 * x + 2 + th.randn(100,1)*2
model = th.nn.Linear(1,1)
model.parameters()
optimizer = th.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(200):
    y_pred= model(x)
    loss = ((y_pred - y) ** 2).mean()
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

print(model.weight)
print(model.bias)





















