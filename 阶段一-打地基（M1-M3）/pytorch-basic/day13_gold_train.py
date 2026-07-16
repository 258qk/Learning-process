from numpy import test
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torch.utils.data import random_split

# ============================================
# TODO 1: transform（和 MNIST 不同：彩色图需要 Resize + 数据增强）
trainform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

testform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

# ============================================
# 训练集：Resize(64,64) → RandomHorizontalFlip → ToTensor → Normalize
# 测试集：Resize(64,64) → ToTensor → Normalize
# 提示：Normalize 三通道用 (0.5, 0.5, 0.5), (0.5, 0.5, 0.5)

# ============================================
# TODO 2: 加载数据（新 API: CIFAR10）
train_data = datasets.CIFAR10(root = 'data/gold',train = True,transform = trainform)
test_data = datasets.CIFAR10(root = 'data/gold',train = False,transform = testform)
# ============================================
# datasets.CIFAR10(root, train, download, transform)
# root='data'，子文件夹名自动变成标签：drone=0, car=1, person=2, bird=3, cat=4, dog=5, frog=6, horse=7, ship=8, truck=9

# ============================================
# TODO 3: DataLoader（和之前一样）
# ============================================
train_loader = DataLoader(train_data ,batch_size = 64 ,shuffle = True)
test_loader = DataLoader(test_data ,batch_size = 64 ,shuffle = False)

# ============================================
# TODO 4: 搭建 CNN（和 MNIST 一样结构，但要适配 3 通道和 64×64 输入）
cnn = nn.Sequential(
    nn.Conv2d(3,32,3,padding = 1),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Conv2d(32,64,3,padding = 1),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Conv2d(64,128,3,padding = 1),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Dropout(0.3),
    nn.Linear(128*4*4, 10),
)
# ============================================
# Conv2d(3,32,3,padding = 1) → ReLU → MaxPool2d(2)  64→32
# Conv2d(32,64,3,padding = 1) → ReLU → MaxPool2d(2)  32→48
# Flatten → Linear(128*4*4, 10)  ← 只有 10 类
# 提示：三个 MaxPool2d(2) 后 64→32→48→128

# ============================================
# TODO 5: loss + optimizer
# ============================================
loss_fn = nn.CrossEntropyLoss()
optim = torch.optim.Adam(cnn.parameters(),lr=0.001,weight_decay = 0.0005)
# ============================================
# TODO 6: 训练循环（和 MNIST 完全一样）
# ============================================
train_losses = []
test_losses = []
for epoch in range(20):
    cnn.train()
    for batch_idx, (x, y) in enumerate(train_loader):
        pred = cnn(x)
        loss = loss_fn(pred,y)
        optim.zero_grad()
        loss.backward()
        optim.step()
        train_losses.append(loss.item())
        test_losses.append(loss.item())
        if batch_idx % 100 == 0:
            print(f"Epoch: {epoch}, Batch: {batch_idx}, Loss: {loss.item():.4f}")

# ============================================
# TODO 7: 测试准确率（和 MNIST 完全一样）
# ============================================
    cnn.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        test_loss = 0
        test_acc = 0
        for x,y in test_loader:
            test_perd = cnn(x)
            correct += (test_perd.argmax(1) == y).sum()
            total += y.size(0)
        test_acc = correct.item() / total
    print(f"Test Accuracy: {test_acc:.4f}") 
train_correct = 0
train_total = 0
with torch.no_grad():
    for x,y in train_loader:
        train_perd = cnn(x)
        train_correct += (train_perd.argmax(1) == y).sum()
        train_total += y.size(0)
    train_acc = train_correct.item() / train_total
    print(f"Train Accuracy: {train_acc:.4f}")


