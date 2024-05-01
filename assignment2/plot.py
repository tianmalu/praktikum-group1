import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline


o2_data = pd.read_csv('o2_cache_miss.csv', sep=';', decimal='.')
o2_data = o2_data.drop(o2_data.columns[0], axis=1)
o2_data = o2_data.drop(o2_data.columns[-1], axis=1)
o3_data = pd.read_csv('o3_cache_miss.csv', sep=';', decimal='.')
o3_data = o3_data.drop(o3_data.columns[0], axis=1)
o3_data = o3_data.drop(o3_data.columns[-1], axis=1)
mflops_data = pd.read_csv('mflops.csv', sep=';', decimal='.')
mflops_data = mflops_data.drop(mflops_data.columns[-1], axis=1)
mflops_data = mflops_data.drop(mflops_data.columns[0], axis=1)

o2_np = o2_data.to_numpy()
o3_np = o3_data.to_numpy()
mflops_np = mflops_data.to_numpy()

x_axis = [500, 1500, 2500, 3500, 4500]

# Smoothing the lines
x_axis_np = np.array(x_axis)
# Line -o2 L2 miss rate
o2_l2 = make_interp_spline(x_axis_np, o2_np[4])
o2_l2_x = np.linspace(x_axis_np.min(), x_axis_np.max(), 500)
o2_l2_y = o2_l2(o2_l2_x)
# Line -o2 L3 miss rate
o2_l3 = make_interp_spline(x_axis_np, o2_np[5])
o2_l3_x = np.linspace(x_axis_np.min(), x_axis_np.max(), 500)
o2_l3_y = o2_l3(o2_l3_x)
# Line -o3 L2 miss rate
o3_l2 = make_interp_spline(x_axis_np, o3_np[4])
o3_l2_x = np.linspace(x_axis_np.min(), x_axis_np.max(), 500)
o3_l2_y = o3_l2(o3_l2_x)
# Line -o3 L3 miss rate
o3_l3 = make_interp_spline(x_axis_np, o3_np[5])
o3_l3_x = np.linspace(x_axis_np.min(), x_axis_np.max(), 500)
o3_l3_y = o3_l3(o3_l3_x)
# Line -o2 Mflops
o2_mflops = make_interp_spline(x_axis_np, mflops_np[0])
o2_mflops_x = np.linspace(x_axis_np.min(), x_axis_np.max(), 500)
o2_mflops_y = o2_mflops(o2_mflops_x)
# Line -o2 Mflops
o3_mflops = make_interp_spline(x_axis_np, mflops_np[1])
o3_mflops_x = np.linspace(x_axis_np.min(), x_axis_np.max(), 500)
o3_mflops_y = o3_mflops(o3_mflops_x)

fig, ax1 = plt.subplots()



ax1.set_xlabel('Resolution')
ax1.set_ylabel('Mflops')
ax1.plot(o2_mflops_x, o2_mflops_y, label='-o2 Mflops', color='b', linestyle='-')
ax1.plot(o3_mflops_x, o3_mflops_y, label='-o3 Mflops', color='g', linestyle='-')
ax1.set_xticks(x_axis)

# Legend for Mflops
plt.legend()

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylabel('L2/L3 Cache Miss Rates (%)')  # we already handled the x-label with ax1
ax2.plot(o2_l2_x, o2_l2_y, label='-o2 L2 Miss Rate', color='r', linestyle='-') # x_axis and o2_np[4]
ax2.plot(o3_l2_x, o3_l2_y, label='-o3 L2 Miss Rate', color='m', linestyle='-')
ax2.plot(o2_l3_x, o2_l3_y, label='-o2 L3 Miss Rate', color='k', linestyle='-')
ax2.plot(o3_l3_x, o3_l3_y, label='-o3 L3 Miss Rate', color='orange', linestyle='-')

fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.legend()
plt.title('Group 1 MFLOPS and L2/L3 Cache Miss Rates with -o2', pad=-10)
plt.savefig('plot.pdf')