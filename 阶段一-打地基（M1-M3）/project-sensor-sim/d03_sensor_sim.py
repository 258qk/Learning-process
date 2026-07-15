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
# 通道4：模拟GPS经纬度
gps = np.linspace(31.23,31.23 + (samples-1) * 0.00001, samples) + 0.00001 * np.random.randn(samples)

# 统计
print("通道1 (加速度X) - 均值: {:.4f}, 峰值: {:.4f}, 方差: {:.6f}".format(accel_x.mean(), np.max(np.abs(accel_x)), accel_x.var()))#
print("通道2 (陀螺仪Z) - 均值: {:.4f}, 峰值: {:.4f}, 方差: {:.6f}".format(gyro_z.mean(), np.max(np.abs(gyro_z)), gyro_z.var()))
print("通道3 (温度)   - 均值: {:.4f}, 峰值: {:.4f}, 方差: {:.6f}".format(temp.mean(), np.max(np.abs(temp - 25)), temp.var()))
print("通道4 (GPS) - 均值：{:.4f}, 峰值：{:.4f}, 方差：{:.6f}".format(gps.mean(), np.max(np.abs(gps - gps.mean())), gps.var()))
# 加速度切片
print(f"加速度100-159 - 均值：{accel_x[100:160].mean():.4f}, 峰值：{np.max(np.abs(accel_x[100:160])):.4f}, 方差：{accel_x[100:160].var():.6f}")
print(f"加速度500-559 - 均值：{accel_x[500:560].mean():.4f}, 峰值: {np.max(np.abs(accel_x[500:560])):.4f}, 方差: {accel_x[500:560].var():.6f}")
# 导出 CSV
data = np.column_stack((accel_x, gyro_z, temp, gps)) # 堆叠数据，将数组按列堆叠
print("data:",data)
np.savetxt(os.path.join(script_dir, "sensor_data.csv"), data, delimiter=",", header="AccelX,GyroZ,Temp,GPS", comments="")
print("\n数据已导出到 sensor_data.csv")

# 画图
plt.figure(figsize=(10, 12))
plt.subplot(611); plt.plot(accel_x[:200]); plt.title("Accel X")
plt.subplot(612); plt.plot(gyro_z[:200]); plt.title("Gyro Z")
plt.subplot(613); plt.plot(temp[:200]); plt.title("Temperature")
plt.subplot(614); plt.plot(gps[:200]); plt.title("GPS")
plt.subplot(615); plt.plot(accel_x[100:160]); plt.title("Accel X 100-159")
plt.subplot(616); plt.plot(accel_x[500:560]); plt.title("Accel X 500-559")
plt.tight_layout(); plt.savefig(os.path.join(script_dir, "sensor_plot.png")); plt.show()
print("波形图已保存到 sensor_plot.png")

#寻找异常点
max_idx = np.argmax(np.abs(accel_x))
print(f"异常点：{max_idx}")
print(f"异常点值：{accel_x[max_idx]:.4f}")

# 自检
np.random.seed(42)
small_samples = 100
new_accel_x = 0 + 0.02 * np.random.randn(small_samples)
print(f"自检加速度均值：{new_accel_x.mean():.4f}, 峰值：{np.max(np.abs(new_accel_x)):.4f}, 方差：{new_accel_x.var():.6f}")

new_gyro_z = 0.1 * np.sin(np.linspace(0,4*np.pi,small_samples)) + 0.01 * np.random.randn(small_samples)
print(f"自检陀螺仪均值：{new_gyro_z.mean():.4f}, 峰值：{np.max(np.abs(new_gyro_z)):.4f}, 方差：{new_gyro_z.var():.6f}")

new_data = np.column_stack((new_accel_x ,new_gyro_z))
np.savetxt(os.path.join(script_dir, "new_data.csv"),new_data,delimiter=',',header="new_accel_x,new_gyro_z",comments="")
plt.figure(figsize=(10, 4))
plt.subplot(211); plt.plot(new_data[:,0]); plt.title("New Accel X")
plt.subplot(212); plt.plot(new_data[:,1]); plt.title("New Gyro Z")
plt.tight_layout(); plt.show()




