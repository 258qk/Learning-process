"""
Day 02: NumPy 数组操作
2026.6.8
"""

import numpy as np

# # a = np.linspace(0,1,10) # 生成 10 个等间距的数，从 0 到 1
# # # linspace函数(开始值,结束值,元素个数)
# # print("a:",a,"\n ")

# # b = np.arange(0,1,0.1) # 从0开始，到1之前停，步长为0.1
# # # arange函数(开始值,结束值,步长)
# # print("b:",b,"\n ")

# # c = np.array([1,2,3,4,5,6,7,8,9,10])
# # print("c:",c,"\n ")
# # print("前五个：",c[:5])
# # print("后五个：",c[-5:])
# # print("中间三个:",c[2:5])
# # # 切片格式：[开始索引:结束索引:步长]
# # print("步长为2:",c[0:4:2])

# #题目1
# #生成 0 到 2π（约 6.28），取 20 个等间距点。用 NumPy 一行搞定，再用 Python 列表手写试试。
# #numpy写法
# print("采样点生成：",np.linspace(0,2*np.pi,20)) # 为什么不能是2*pi?,必须要是2*np.pi,否则会报错
# #题目5用 Python 列表实现题目 1（生成 0 到 2π 之间 20 个等间距点），对比两边的代码行数。感受一下为什么 AI 领域不用 Python 列表。
# #python写法
# result = []
# for i in range(20):
#     result.append(i*2*np.pi/19)
# print("采样点生成：",result)



# # 题目 2：批量运算
# # numpy写法：
# data = np.array([3, 7, 2, 9, 1, 5, 8, 4, 6, 0])
# print("data:",data)
# print("data的平均值:",np.mean(data))
# print("data的最大值:",np.max(data))
# print("data的最小值:",np.min(data))
# print("data的总和:",np.sum(data))
# print("data的乘积:",np.prod(data))
# print("data的方差:",np.var(data))
# #python写法：
# data_1 = [1,2,3,4,5,6,7,8,9,10]
# print("均值:",sum(data_1)/len(data_1))
# print("最大值:",max(data_1))
# print("最小值:",min(data_1))



# #题目 3：切片操作

# arr = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# print("arr的前3个元素:",arr[:3])
# print("arr的最后4个元素:",arr[-4:])
# print("arr中间第4个到第7个元素:",arr[3:7])
# print("步长为2时:",arr[0:10:2])
# #brr = brray[100,200,300,400,500,600,700,800,900,1000]
# # print("brr的前三个元素:",brr[0:3]) #报错

# # 题目 4：数学运算
# data_2= np.array([1,4,9,16,25])
# print("每个元素开根号：",np.sqrt(data_2))
# print("每个元素平方：",np.square(data_2))
# data_3 = (data_2+1)/2
# print("每个元素加1后除以2:",data_3)


# # 1. reshape：改变数组形状
# arr = np.arange(1, 13)           # [1,2,3,...,12]
# print("原数组:", arr)
# print("变 3×4:\n", arr.reshape(3, 4))
# print("变 4×3:\n", arr.reshape(4, 3))

# # 2. 广播：不同形状也能运算
# data = np.array([[1, 2, 3],
#                  [4, 5, 6]])
# bias = np.array([10, 20, 30])    # 形状是 (3,)
# print("\n每行加 bias:\n", data + bias)  # bias 自动扩展到两行

# # 3. 统计函数：沿某个方向算
# mat = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# print("\n全部求和:", mat.sum())
# print("每列求和 (axis=0):", mat.sum(axis=0))   # 竖着加 → [5, 7, 9]
# print("每行求和 (axis=1):", mat.sum(axis=1))   # 横着加 → [6, 15]

# 题目 1：reshape 实战
data_1 = np.arange(1,25)
print("data_1 6*4 每行平均值:\n",data_1.reshape(6,4).mean(axis = 1))
print("data_1 4*6 每行平均值:\n",data_1.reshape(4,6).mean(axis = 1))
print("data_1 2*12 每行平均值:\n",data_1.reshape(2,12).mean(axis = 1))

#题目 2：广播真实场景
#数据
samples = np.array([[0.5, 1.2, 0.8, 2.1],
                    [0.6, 1.1, 0.7, 2.0],
                    [0.4, 1.3, 0.9, 2.2],
                    [0.7, 1.0, 0.6, 1.9],
                    [0.5, 1.2, 0.8, 2.1]])
#偏移量
offset = np.array([0.1, -0.05, 0.0, 0.15])
#广播
print("广播后的数据:\n",samples - offset)

# 题目 3：axis 方向判断
mat = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])
print("mat:",mat)
print("mat的每列求和\n",mat.mean(axis = 0)) 
print("mat的每行求和\n",mat.mean(axis = 1)) 










