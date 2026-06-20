import matplotlib.pyplot as plt
import numpy as np

# t = np.linspace(0 , 2*np.pi, 20)

# accel = np.sin(t) + 0.1 * np.random.randn(20)
# gyro = np.cos(t) + 0.1 * np.random.randn(20)

# fig, ax1 = plt.subplots(figsize = (10,5))
# ax2 = ax1.twinx()
# ax1.plot(t, accel ,label = "accel",color = "blue")
# ax1.set_xlabel("time")
# ax1.set_ylabel("accel")
# ax1.legend()

# ax2.plot(t,gyro,label = "gyro",color = "red")
# ax2.set_ylabel("gyro")
# ax2.legend()

# plt.show()


# 自检

x = np.linspace(0,10,50)
y = 3 * x + 2 + np.random.randn(50) * 3

w_history = np.linspace(0.5, 2.8, 20)
b_history = np.linspace(0.2, 2.3, 20)

fig = plt.figure(figsize = (10, 6))

ax1 = fig.add_subplot(1,2,1)
ax1.plot(x ,y ,label = "true",color = "blue")
ax1.legend()
ax1.set_xlabel("x")
ax1.set_ylabel("y")

ax2 = fig.add_subplot(1,2,2)
ax2.plot(range(20),w_history,label = "w",color = "blue")
ax2.set_xlabel("step")
ax2.set_ylabel("w")

ax3 = ax2.twinx()
ax3.plot(range(20),b_history,label = "b",color = "red")
ax3.set_xlabel("step")
ax3.set_ylabel("b")
ax3.legend()

plt.show()


