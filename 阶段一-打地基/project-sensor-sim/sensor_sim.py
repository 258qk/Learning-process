import numpy as np
import matplotlib.pyplot as plt
import os

# 确保输出文件存到脚本所在目录，而不是执行目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 模拟 3 个传感器通道，1000 个采样点（就像你接了 3 路 ADC，采了 1000 次）
np.random.seed(42)  # 固定随机种子，每次跑结果一样（调试用）
samples = 1000

# 通道1：模拟加速度计 X 轴（静止 + 微小振动噪声）
accel_x = 0.02 * np.random.randn(samples)
# 通道2：模拟陀螺仪 Z 轴（缓慢漂移 + 噪声）
gyro_z = 0.1 * np.sin(np.linspace(0, 4*np.pi, samples)) + 0.01 * np.random.randn(samples)
# 通道3：模拟温度传感器（25°C 基准 + 噪声）
temp = 25 + 0.3 * np.random.randn(samples)

# 统计
print("通道1 (加速度X) - 均值: {:.4f}, 峰值: {:.4f}, 方差: {:.6f}".format(accel_x.mean(), np.max(np.abs(accel_x)), accel_x.var()))
print("通道2 (陀螺仪Z) - 均值: {:.4f}, 峰值: {:.4f}, 方差: {:.6f}".format(gyro_z.mean(), np.max(np.abs(gyro_z)), gyro_z.var()))
print("通道3 (温度)   - 均值: {:.4f}, 峰值: {:.4f}, 方差: {:.6f}".format(temp.mean(), np.max(np.abs(temp - 25)), temp.var()))

# 导出 CSV
data = np.column_stack((accel_x, gyro_z, temp))
np.savetxt(os.path.join(script_dir, "sensor_data.csv"), data, delimiter=",", header="AccelX,GyroZ,Temp", comments="")
print("\n数据已导出到 sensor_data.csv")

# 画图
plt.figure(figsize=(10, 6))
plt.subplot(311); plt.plot(accel_x[:200]); plt.title("Accel X")
plt.subplot(312); plt.plot(gyro_z[:200]); plt.title("Gyro Z")
plt.subplot(313); plt.plot(temp[:200]); plt.title("Temperature")
plt.tight_layout(); plt.savefig(os.path.join(script_dir, "sensor_plot.png")); plt.show()
print("波形图已保存到 sensor_plot.png")
