import matplotlib.pyplot as plt

# Data
resolutions = [500, 1500, 2500, 3500, 4500]

mflops_O0 = [425.17, 299.92, 276.72, 252.79, 245.49]
mflops_O1 = [1395.02, 784.87, 667.71, 583.39, 567.66]
mflops_O2 = [1617.82, 850.96, 680.40, 649.72, 668.80]
mflops_O3 = [1663.39, 831.35, 702.53, 651.39, 666.43]
mflops_Ofast = [1724.12, 881.99,  698.23,  662.11, 677.39]
mflops_xhost = [1673.23 , 975.63, 729.88,  664.22, 685.21]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(resolutions, mflops_O0, marker='o', label='O0')
plt.plot(resolutions, mflops_O1, marker='o', label='O1')
plt.plot(resolutions, mflops_O2, marker='o', label='O2')
plt.plot(resolutions, mflops_O3, marker='o', label='O3')
plt.plot(resolutions, mflops_Ofast, marker='o', label='Ofast')
plt.plot(resolutions, mflops_xhost, marker='o', label='xhost')

plt.title('-O MFLOPS Performance Trends')
plt.xlabel('Resolution')
plt.ylabel('MFLOPS')
plt.xticks(resolutions)  # Ensuring x-axis only shows the given resolutions
plt.legend()
plt.grid(True)
plt.savefig('mflops_trends.png')
