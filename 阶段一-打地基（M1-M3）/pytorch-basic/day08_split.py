import torch
from torch.utils.data import TensorDataset, DataLoader, random_split

x = torch.linspace(0, 10, 200).unsqueeze(1)
y = 3 * x + 2 + torch.randn(200, 1) * 2

dataset = TensorDataset(x, y)
train_size = int(0.7 * len(dataset))
test_size = len(dataset) - train_size

train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
print(f"训练集: {len(train_dataset)} 条, 测试集: {len(test_dataset)} 条")

train_dataloader = DataLoader(train_dataset ,batch_size = 20, shuffle = True)
test_dataloader = DataLoader(test_dataset, batch_size = 20)

model = torch.nn.Linear(1,1)
optimizer = torch.optim.SGD(model.parameters() ,lr = 0.01)

train_losses = []
test_losses = []

for epoch in range(200):
    # ---- 训练 ----
    model.train()
    for batch_x, batch_y in train_dataloader:
        y_pred = model(batch_x)
        loss = ((y_pred - batch_y) ** 2).mean()
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

    # ---- 评估（不打分，只看看当前水平）----
    model.eval()
    with torch.no_grad():
        # 训练集 loss
        train_x = x[train_dataset.indices]
        train_pred = model(train_x)
        train_y = y[train_dataset.indices]
        train_loss = ((train_pred - train_y) ** 2).mean().item()

        # 测试集 loss（用没见过的数据）
        test_indices = test_dataset.indices       # 被抽中的 60 个下标
        test_x = x[test_indices]                  # 测试集的 x
        test_y = y[test_indices]                  # 测试集的 y                 # 模型预测
        test_pred = model(test_x)
        test_loss = ((test_pred - test_y) ** 2).mean().item()

    train_losses.append(train_loss)
    test_losses.append(test_loss)
    
    if epoch % 40 == 0:
        print(f"Epoch {epoch:3d}: train_loss={train_loss:.4f}, test_loss={test_loss:.4f}")

print(f"\n最终: train_loss={train_losses[-1]:.4f}, test_loss={test_losses[-1]:.4f}")
print(f"w={model.weight.item():.2f}, b={model.bias.item():.2f}")
print(f"目标: w=3.00, b=2.00")