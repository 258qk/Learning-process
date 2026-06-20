# API 速查手册 — 阶段一（M1-M3）

> 更新日期：2026-06-18 | 覆盖：Day 01-07 + 青铜项目

---

## 一、NumPy（numpy as np）

### 1.1 创建数组

| 函数 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `np.array([1,2,3])` | `object`：Python 列表或嵌套列表 | `ndarray` | 创建 NumPy 数组。C 类比：`int arr[] = {1,2,3}` |
| `np.array([[1,2],[3,4]])` | `object`：二维列表 | `ndarray (2D)` | 创建矩阵 |
| `np.ones(5)` | `shape`：int 或 tuple | `ndarray` | 全 1 数组。`ones(5)` → `[1.,1.,1.,1.,1.]` |
| `np.zeros(5)` | `shape`：int 或 tuple | `ndarray` | 全 0 数组。`zeros(5)` → `[0.,0.,0.,0.,0.]` |
| `np.linspace(0, 10, 50)` | `start`：起点 / `stop`：终点 / `num`：元素个数 | `ndarray` | 等间距数组。**你定点数，它算步长**。`linspace(0,10,50)` = 从 0 到 10 等距生成 50 个点 |
| `np.arange(0, 1, 0.1)` | `start`：起点 / `stop`：终点（不含）/ `step`：步长 | `ndarray` | 等差数列。**你定步长，它算个数**。和 `linspace` 互补 |
| `np.random.randn(100)` | `d0, d1, ...`：各维度大小 | `ndarray` | 标准正态分布随机数（均值 0，标准差 1） |
| `np.random.randn(100, 1)` | `d0=100, d1=1` | `ndarray (100,1)` | 100 行 1 列的随机矩阵 |
| `np.random.seed(42)` | `seed`：int，随机种子 | `None`（无返回值） | **固定随机数，每次跑结果一样。调试必备，不加 seed=每次数据不同** |

### 1.2 数学运算

| 函数 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `np.sin(x)` | `x`：ndarray 或数值 | `ndarray` 或 `float` | 正弦，逐个元素计算。如 `np.sin(np.pi/2)` = 1.0 |
| `np.cos(x)` | `x`：ndarray 或数值 | `ndarray` 或 `float` | 余弦 |
| `np.sqrt(x)` | `x`：ndarray 或数值 | `ndarray` 或 `float` | 开根号 |
| `np.square(x)` | `x`：ndarray 或数值 | `ndarray` 或 `float` | 平方 |
| `np.abs(x)` | `x`：ndarray 或数值 | `ndarray` 或 `float` | 绝对值。`abs(-3)` = 3 |
| `np.max(x)` | `x`：ndarray | 标量 | 最大值（全部元素） |
| `np.pi` | — | `float (3.14159...)` | 圆周率常量 |
| `np.radians(30)` | `degrees`：角度 | `float` | 角度 → 弧度 |

### 1.3 统计方法（ndarray 的成员方法）

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `arr.mean()` | 无参数 → 全部求平均 | 标量 | 平均值。`[1,2,3].mean()` = 2.0 |
| `arr.mean(axis=0)` | `axis`：0=沿行方向（每列），1=沿列方向（每行） | `ndarray` | 按方向求平均。`axis=0` = "上下方向压缩"，每列一个结果 |
| `arr.mean(axis=1)` | `axis=1` | `ndarray` | 每行一个平均值 |
| `arr.sum()` | 无参数 → 全部求和 | 标量 | 求和。`[1,2,3].sum()` = 6 |
| `arr.sum(axis=0)` | `axis=0` | `ndarray` | 每列求和 |
| `arr.sum(axis=1)` | `axis=1` | `ndarray` | 每行求和 |
| `arr.std()` | 无参数 | 标量 | **标准差——描述数据分散程度。std 越大，数据越散** |
| `arr.var()` | 无参数 | 标量 | 方差（标准差的平方） |
| `arr.max()` | 无参数 | 标量 | 最大值 |
| `arr.min()` | 无参数 | 标量 | 最小值 |
| `arr.prod()` | 无参数 | 标量 | 乘积。`[2,3,4].prod()` = 24 |

### 1.4 数组操作

| 方法/函数 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `arr.argmax()` | 无参数 | `int`（下标） | **返回最大值的下标，不是最大值本身**。`[3,7,2].argmax()` = 1 |
| `arr.reshape(2, 3)` | `new_shape`：新形状 tuple | `ndarray` | 改变形状。**前提：元素总数不变**。6 个元素可 reshape(2,3)，不可 reshape(2,4) |
| `arr.T` | — | `ndarray` | 转置（行变列，列变行）。**属性，不加括号** |
| `arr @ arr2` | — | `ndarray` | 矩阵乘法（不是 `*`）。`*` 是逐元素乘 |
| `np.column_stack((a, b))` | `tup`：tuple of ndarray | `ndarray` | **横向拼接两个数组。要求：两个数组行数相同**。青铜项目用过 |
| `np.savetxt("a.csv", arr)` | `fname`：文件路径 / `X`：ndarray / `delimiter`：分隔符 / `header`：表头字符串 / `comments`：注释符 | `None` | **保存数组到 CSV 文件。青铜项目用过** |

### 1.5 属性和规则

| 属性 | 说明 |
|------|------|
| `arr.shape` | 返回形状元组。`(100, 4)` = 100 行 4 列。**属性，不加括号。加了报错 `not callable`** |
| `arr.dtype` | 数据类型。`(100, 4)` = 100 行 4 列 |
| **axis=0** | 沿行方向压缩 → 每列一个结果（"竖着算"） |
| **axis=1** | 沿列方向压缩 → 每行一个结果（"横着算"） |
| **广播规则** | 不同 shape 运算时自动扩展。如 `(2,3) + (3,)` = 每行加 bias。**前提：维度对齐** |

### 1.6 Python vs NumPy 对比

| 操作 | Python 列表 | NumPy |
|------|-----------|-------|
| 每个元素 +10 | `for i in range(len(arr)): arr[i] += 10` | `arr + 10` |
| 求平均值 | `sum(arr)/len(arr)` | `arr.mean()` |
| 矩阵乘法 | 自己写循环 | `A @ B` |

---

## 二、PyTorch Tensor（torch）

### 2.1 创建 Tensor

| 函数 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `torch.tensor([1,2,3])` | `data`：列表/ndarray/标量 | `Tensor` | 创建张量。**不是"元组"（元组是 Python tuple）** |
| `torch.tensor(np_array)` | `data`：ndarray | `Tensor` | NumPy → Tensor |
| `torch.tensor(0.0, requires_grad=True)` | `data` + `requires_grad` | `Tensor` | 创建可训练参数 |
| `torch.linspace(0, 10, 50)` | 同 np.linspace | `Tensor` | PyTorch 版 linspace |
| `torch.randn(100, 1)` | `size`：各维度 | `Tensor` | PyTorch 版正态分布随机数 |

### 2.2 Tensor 方法

| 方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `tensor.numpy()` | 无参数 | `ndarray` | **Tensor → NumPy。方向：Tensor 调 .numpy() 得 ndarray，不是 NumPy 调 .tensor()** |
| `tensor.item()` | 无参数 | Python 标量（float/int） | **单值 Tensor 取数字。多值 Tensor 调用会报错** |
| `tensor.unsqueeze(1)` | `dim`：在哪加维度 | `Tensor` | **加一个维度。`(100,)` → `(100,1)`。C 类比：`float[100]` → `float[100][1]`** |
| `tensor.squeeze()` | 无参数 | `Tensor` | 去掉所有大小为 1 的维度。`(100,1)` → `(100,)` |
| `tensor.tolist()` | 无参数 | Python list | Tensor → Python 列表，打印用 |
| `tensor.detach()` | 无参数 | `Tensor`（切断计算图） | **撕掉 autograd 追踪标签，数值不变。C 类比：断指针溯源** |
| `tensor.clone()` | 无参数 | `Tensor`（独立副本） | **深拷贝。不 clone 存的是引用，原值变它也变。C 类比：malloc + memcpy** |
| `tensor.mean()` | 无参数或 `dim=` | `Tensor` | 同 NumPy |
| `tensor.mean(dim=0)` | `dim`：PyTorch 版 axis | `Tensor` | **注意：PyTorch 用 `dim`，NumPy 用 `axis`，意思一样** |

### 2.3 Tensor 属性

| 属性 | 说明 |
|------|------|
| `tensor.shape` | **属性，不加括号。`x.shape()` 报错 `'torch.Size' object is not callable`** |
| `tensor.dtype` | 数据类型 |
| `tensor.grad` | **autograd 梯度值。⚠️ 前置依赖：必须先调用 `.backward()`，否则 `.grad` 是 None** |

---

## 三、PyTorch autograd（自动求导）

| 函数/方法 | 参数 | 返回值 | 副作用 | 说明 |
|------|------|--------|--------|------|
| `torch.tensor(0.0, requires_grad=True)` | `requires_grad=True` | `Tensor` | 打开"操作录音" | 告知 PyTorch 追踪这个变量的运算过程 |
| `loss.backward()` | 无参数 | `None` | **对所有 `requires_grad=True` 的变量计算梯度，填入 `.grad`** | 倒放录音，算出导数。C 类比：函数调用栈回溯 |
| `tensor.grad` | — | `Tensor` 或 `None` | — | **⚠️ 前置依赖：必须先调 `backward()`，否则是 None** |
| `with torch.no_grad():` | 上下文管理器 | — | 块内操作不追踪 | **更新参数时用（手写 `w -= lr*grad` 必须包，optimizer.step() 可包可不包）** |
| `tensor.grad.zero_()` | 无参数 | `None` | 梯度归零 | **⚠️ 每次更新后必须清零，否则梯度累加（PyTorch 默认 += 不是 =）** |
| `optimizer.zero_grad()` | 无参数 | `None` | 清零所有参数的梯度 | **PyTorch 标准训练循环必备，替代手写的 `w.grad.zero_()`** |

### autograd 核心原理

```
录音阶段：y_pred = w*x + b  →  loss = ((y_pred-y)**2).mean()
          PyTorch 记录每个操作，形成计算图

倒放阶段：loss.backward()
          PyTorch 从 loss 出发，倒着算出：
            loss → y_pred → w（得 w.grad）
            loss → y_pred → b（得 b.grad）

更新阶段：w -= lr * w.grad（沿梯度方向走一步）
```

### 训练循环标准模板

```python
for epoch in range(N):
    y_pred = model(x)               # 预测（录音中）
    loss = ((y_pred - y)**2).mean()  # 损失（录音中）
    loss.backward()                  # 求梯度（倒放）
    optimizer.step()                 # 更新参数（不录音）
    optimizer.zero_grad()            # 清零梯度（不录音）
```

---

## 四、PyTorch nn.Module（模型层）

### 4.1 nn.Linear

| 函数 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `nn.Linear(1, 1)` | `in_features`：输入特征数 / `out_features`：输出特征数 | `nn.Linear` 对象 | **一行替代手写的 w 和 b。`(1,1)` = 1 个 x → 1 个 y** |
| `nn.Linear(3, 1)` | in=3, out=1 | `nn.Linear` 对象 | 3 个 x → 1 个 y。内部自动生成 w1,w2,w3 和 b |

**关键规则：Linear 的参数是特征数，不是样本数。50 条数据只约有 1 个 x 特征 → `Linear(1, 1)`，不是 `Linear(50, 1)`。**

### 4.2 nn.Linear 属性和方法

| 属性/方法 | 说明 |
|------|------|
| `model.weight` | w 参数（Tensor）。`model.weight.item()` 取单值 |
| `model.bias` | b 参数（Tensor）。`model.bias.item()` 取单值 |
| `model.parameters()` | 返回所有可训练参数（生成器对象，不能直接 print） |
| `list(model.parameters())` | **将生成器转成列表才能打印，否则只看到内存地址** |
| `model(x)` | 前向计算。`nn.Linear(1, 1)` → 执行 `y = w*x + b` |

### 4.3 w/b 初始值

- PyTorch 自动**随机初始化**（均匀分布）
- 每次运行结果不同
- 可手动设：`model.weight.data = torch.tensor([[2.0]])`（一般不这么做）

---

## 五、PyTorch Optimizer（优化器）

| 函数/方法 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `torch.optim.SGD(params, lr=0.01)` | `params`：`model.parameters()` / `lr`：学习率 | `Optimizer` 对象 | **自动更新参数。SGD = Stochastic Gradient Descent（随机梯度下降）** |
| `optimizer.step()` | 无参数 | `None` | **对每个参数执行 `param = param - lr * param.grad`。替代手写 `w -= lr*grad`** |
| `optimizer.zero_grad()` | 无参数 | `None` | **清零所有参数梯度。替代手写 `w.grad.zero_()`** |

### optimizer 机制

```python
# optimizer 不是存 w 和 b 的值，是记住：更新谁 + 用什么规则 + 步长多大
# w 和 b 的值始终在 model 里，optimizer 只是拿了 model 的"钥匙"
# 每次 optimizer.step() 时，带着钥匙去 model 里把 w 和 b 改了

# hand-written (Day 05):
with torch.no_grad():
    w -= 0.01 * w.grad
    b -= 0.01 * b.grad
w.grad.zero_()
b.grad.zero_()

# optimizer (Day 07):
optimizer.step()       # 一步替代上面 2 行更新
optimizer.zero_grad()  # 一步替代上面 2 行清零
```

### 关于 no_grad

- optimizer.step() **内部绕过 autograd**，不需要包 `no_grad()`
- 包了也没错，不包也不报错
- 手写 `w -= lr*grad` 才必须包 `no_grad()`

---

## 六、PyTorch DataLoader（数据加载）

| 类/方法 | 参数 | 说明 |
|------|------|------|
| `TensorDataset(x, y)` | `*tensors`：多个 Tensor（数据和标签） | **把 x 和 y 绑在一起。`dataset[0]` → `(x值, y值)` 元组** |
| `len(dataset)` | — | 返回样本总数 |
| `DataLoader(dataset, batch_size=20, shuffle=True)` | `dataset`：数据集 / `batch_size`：每批几条 / `shuffle`：是否打乱 | **自动切 batch + 打乱 + 分发。不是数组，是迭代器** |
| `len(loader)` | — | batch 数量。100 条 ÷ batch_size=20 → 5 个 batch |

### 迭代访问（不能用下标，只能用 for）

```python
# ✅ 正确写法：
for batch_x, batch_y in loader:      # 每次返回 (x批量, y批量)
    ...

# ❌ 错误写法：
for i in range(len(loader)):
    print(batch_x)    # NameError！batch_x 从未被赋值

# ✅ 带编号：
for i, (batch_x, batch_y) in enumerate(loader):
    ...
```

**loader 是迭代器不是数组，不能下标访问。batch_x 和 batch_y 是 for 循环自动解包出来的。** C 类比：`for(ptr=list; ptr!=NULL; ptr=ptr->next)` — 每次取一块，不知道第几块。

---

## 七、matplotlib（matplotlib.pyplot as plt）

| 函数 | 参数 | 返回值 | 说明 |
|------|------|--------|------|
| `plt.figure(figsize=(10, 6))` | `figsize`：画布大小 (宽, 高) 英寸 | `Figure` 对象 | 创建画布 |
| `plt.plot(x, y)` | `x, y`：坐标数据 | `Line2D` 列表 | 画折线 |
| `plt.plot(x, y, alpha=0.5, color="red", label="名称")` | `alpha`：透明度 0-1 / `color`：颜色 / `label`：图例标签 | — | 带样式的折线 |
| `plt.scatter(x, y)` | `x, y`：坐标数据 | `PathCollection` | 画散点 |
| `plt.scatter(x, y, alpha=0.5, s=10, label="名称")` | `alpha`：透明度 / `s`：点大小 | — | 带样式的散点 |
| `plt.subplot(211)` | `nrows, ncols, index` 或 3 位数 | `Axes` | 子图。`211` = 2 行 1 列第 1 个 / `212` = 2 行 1 列第 2 个 |
| `plt.subplot(611)` | 6 行 1 列第 1 个 | `Axes` | 最多可叠多层子图 |
| `plt.xlabel("x")` | `xlabel`：字符串 | — | X 轴标签 |
| `plt.ylabel("y")` | `ylabel`：字符串 | — | Y 轴标签 |
| `plt.title("标题")` | `label`：字符串 | — | 图标题 |
| `plt.legend()` | — | — | 显示图例（前提：之前用过 `label=`） |
| `plt.tight_layout()` | — | — | **自动调整子图间距，防止标签重叠。画 subplot 时必加** |
| `plt.savefig("path.png")` | `fname`：文件路径 | — | 保存图片到文件 |
| `plt.show()` | — | — | 显示图片 |

### 常用颜色对照
`"red"` `"blue"` `"green"` `"black"` `"gray"` `"orange"` `"purple"`

---

## 八、Python 标准库

| 函数/模块 | 说明 |
|------|------|
| `import os` | 操作系统接口 |
| `os.path.dirname(os.path.abspath(__file__))` | **获取当前脚本所在目录的绝对路径。保存文件时避免 CWD 问题** |
| `os.path.join(dir, "file.csv")` | 拼接路径，自动处理 `/` 和 `\` |
| `len(x)` | 返回长度（适用于 list/ndarray/Tensor/Dataset/DataLoader） |
| `list(x)` | 把生成器/迭代器转成列表，才能打印内容 |
| `range(N)` | `for i in range(5)` → `i = 0,1,2,3,4`。C 类比：`for(int i=0; i<N; i++)` |
| `enumerate(obj)` | `for i, val in enumerate(lst)` → `i`=下标, `val`=值 |
| `f-string` | `f"w = {w.item():.2f}"` → `:.2f` 保留 2 位小数 |
| `.format()` | `"{:.4f}".format(val)` → 旧式格式化，和 f-string 等价 |
| `np.array([[1,2],[3,4]])` — `arr[0:2, 1:3]` | **二维切片 `[行范围, 列范围]`。规则：起始位 = N-1，停止位 = N。C 类比：`for(i=0;i<n;i++)`** |

### Python 切片规则

```python
arr[0:5]     # 下标 0~4（不含 5）
arr[:3]      # 前 3 个
arr[-3:]     # 最后 3 个
arr[1:4]     # 下标 1~3
arr[::2]     # 步长 2（隔一个取一个）
arr[1:4, :2] # 二维：第 1-3 行，前 2 列
```

---

## 九、训练循环模板速查

### 模板 A：手写参数（Day 04-05）

```python
w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)

for epoch in range(N):
    y_pred = w * x + b
    loss = ((y_pred - y)**2).mean()
    loss.backward()
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad
    w.grad.zero_()
    b.grad.zero_()
```

### 模板 B：nn.Module + Optimizer（Day 07）★ 推荐

```python
model = nn.Linear(1, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(N):
    y_pred = model(x)
    loss = ((y_pred - y)**2).mean()
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
```

---

## 十、常见报错速查

| 报错 | 原因 | 解决 |
|------|------|------|
| `'torch.Size' object is not callable` | `x.shape()` 加了括号 | `x.shape`（属性不加括号） |
| `NameError: name 'batch_x' is not defined` | `for i in range(len(loader))` 没给 batch_x 赋值 | 改用 `for batch_x, batch_y in loader` |
| `all tensors must share the same first dimension` | `column_stack` 行数不一致 | 检查两数组行数 |
| `nan` 输出 | 梯度爆炸（数据范围大 + 学习率大） | 缩小 x 范围 + 降低学习率 |
| `.item()` 报错 | 多值 Tensor 调 item() | 只有单值能用 item() |
| `requires_grad=True` 不生效 | loss 计算在 `no_grad()` 里 | loss 必须在 no_grad 外面 |
| 循环中 w 越来越离谱 | 忘了 `zero_()` | 梯度累加，每次循环末尾清零 |
