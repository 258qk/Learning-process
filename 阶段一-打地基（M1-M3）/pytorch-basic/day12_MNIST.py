import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# ============================================
transform = transforms.ToTensor()
# ============================================
# TODO 2: 加载 MNIST 数据集
train_data = datasets.MNIST(root='./data', train=True, download=True, transform = transform)
test_data = datasets.MNIST(root='./data', train=False, download=True, transform = transform)
# 用 datasets.MNIST(root='./data', train=True, download=True, transform=刚才定义的)
# 测试集同理，train=False

# ============================================
# TODO 3: 创建 DataLoader
train_loader = DataLoader( train_data,batch_size = 64 , shuffle = True)
test_loader = DataLoader(test_data, batch_size = 64,shuffle = True)
# batch_size=64, shuffle=True（训练集）；测试集 shuffle=True

# ============================================
# TODO 4: 搭建 CNN 模型（用 nn.Sequential）
cnn = nn.Sequential(
  nn.Conv2d(1,8,3,padding=1),
  nn.ReLU(),
  nn.MaxPool2d(2),
  nn.Conv2d(8,16,3,padding=1),
  nn.ReLU(),
  nn.MaxPool2d(2),
  nn.Flatten(),
  nn.Linear(16*7*7, 10),
)

# ============================================
# 结构：Conv2d(1,8,3,padding=1) → ReLU → MaxPool2d(2)
#       → Conv2d(8,16,3,padding=1) → ReLU → MaxPool2d(2)
#       → Flatten() → Linear(784, 10)
#
# ============================================
# TODO 5: 定义 loss 和 optimizer
loss_fn = nn.CrossEntropyLoss()
optim = torch.optim.Adam(cnn.parameters(),lr=0.001)
# ============================================
# loss: CrossEntropyLoss
# optimizer: Adam, lr=0.001

# ============================================
# TODO 6: 训练循环（3 epoch）
train_losses = []
test_losses = []
for epoch in range(3):
    cnn.train()
    for batch_idx, batch in enumerate(train_loader):
        x ,y = batch
        pred = cnn(x)
        loss = loss_fn(pred, y)
        loss.backward()
        optim.step()
        train_losses.append(loss.item())
        optim.zero_grad()
        if batch_idx % 100 == 0:
            print(f'Epoch {epoch}, Batch {batch_idx}, Loss: {loss.item():.4f}')
    cnn.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for x_test,y_test in test_loader:
            pred_test = cnn(x_test) 
            correct += (pred_test.argmax(1) == y_test).sum().item()
            total += y_test.size(0)
            test_loss = loss_fn(pred_test,y_test)
            test_losses.append(test_loss.item())
    print(f'Epoch {epoch}, Test Loss: {test_loss.item():.4f}, Test Accuracy: {correct/total:.4f}')


