import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# 数据
sizes = np.array([500, 1500, 2500, 3500, 4500])

# 第一个数据集
l2_tcm_1 = np.array([7482883, 64608178, 203842617, 378330386, 596010233])
l2_tca_1 = np.array([43488233, 384406863, 1064493291, 2085150618, 3444762593])
l3_tcm_1 = np.array([77430, 20889924, 143061371, 304812337, 503749000])
l3_tca_1 = np.array([7482883, 64608178, 203842617, 378330386, 596010233])
l2_mr_1 = np.array([17.22, 16.80, 19.12, 18.14, 17.30])
l3_mr_1 = np.array([1.03, 32.33, 70.18, 80.57, 84.52])

# 第二个数据集
l2_tcm_2 = np.array([7461458, 63680190, 201710000, 376906642, 588726160])
l2_tca_2 = np.array([43608315, 383911718, 1064489549, 2085036556, 3444812012])
l3_tcm_2 = np.array([106813, 24384433, 143114919, 307602882, 506631529])
l3_tca_2 = np.array([7461458, 63680190, 201710000, 376906642, 588726160])
l2_mr_2 = np.array([17.10, 16.58, 18.94, 18.07, 17.08])
l3_mr_2 = np.array([1.43, 38.29, 70.95, 81.61, 86.06])

# 平滑曲线
x_smooth = np.linspace(sizes.min(), sizes.max(), 500)

# 绘图
plt.figure(figsize=(10, 6))

# L2 Miss Rate
plt.plot(sizes, l2_mr_1, marker='o', label='L2_MR_L2', linestyle='-', color='blue')
plt.plot(sizes, l2_mr_2, marker='o', label='L2_MR_L3', linestyle='-', color='orange')

# L3 Miss Rate
plt.plot(sizes, l3_mr_1, marker='o', label='L3_MR_L2', linestyle='-', color='green')
plt.plot(sizes, l3_mr_2, marker='o', label='L3_MR_L3', linestyle='-', color='red')

plt.title('L2/L3 Miss Rate')
plt.xlabel('Problem Sizes')
plt.ylabel('Miss Rate (%)')
plt.xticks(sizes)
plt.grid(True)
plt.legend()
plt.savefig('test.pdf')
