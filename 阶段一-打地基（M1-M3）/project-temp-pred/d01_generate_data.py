import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

np.random.seed(42)

hours = 24 * 7
t = np.arange(hours)

daily_cycle = 8 * np.sin(2 * np.pi * t / 24 - np.pi/2) + 15

trend = 0.05 * t

noise = np.random.randn(hours) * 1.5

temp = daily_cycle + trend + noise

np.savetxt(os.path.join(script_dir, "temperature_data.csv"),
           temp.reshape(-1, 1),
           delimiter=",",
           header="temperature",
           comments="")

print(f"生成温度数据 {len(temp)} 条（{len(temp)//24} 天）")
print(f"温度范围：{temp.min():.1f}°C ~ {temp.max():.1f}°C")
print(f"已保存：temperature_data.csv")
