import matplotlib.pyplot as plt

# Data for each optimization flag combination
resolutions = [500, 1500, 2500, 3500, 4500]

mflops_O3_ipo = [1755.65, 1079.96, 716.44, 631.94, 637.58]
mflops_O3_ipo_fno_alias = [1766.93, 992.19, 697.46, 629.50, 632.93]
mflops_O3_ipo_fno_alias_xcore_avx512 = [1769.57, 823.52, 702.72, 653.86, 671.55]
mflops_O3_fno_alias_xcore_avx512 = [5075.89, 3822.51, 2879.16, 2797.12, 2798.91]
mflops_O3_ipo_xcore_avx512 = [1734.61, 823.75, 692.83, 656.86, 672.34]
mflops_O3_xcore_avx512 = [1671.99, 787.87, 698.01, 653.61, 680.31]
mflops_O3_fno_alias = [3663.87, 3296.52, 2630.16, 2579.79, 2600.29]

# Plotting
plt.figure(figsize=(14, 8))
plt.plot(resolutions, mflops_O3_ipo, marker='o', label='-O3 -ipo')
plt.plot(resolutions, mflops_O3_ipo_fno_alias, marker='o', label='-O3 -ipo -fno-alias')
plt.plot(resolutions, mflops_O3_ipo_fno_alias_xcore_avx512, marker='o', label='-O3 -ipo -fno-alias -xCORE-AVX512')
plt.plot(resolutions, mflops_O3_fno_alias_xcore_avx512, marker='o', label='-O3 -fno-alias -xCORE-AVX512')
plt.plot(resolutions, mflops_O3_ipo_xcore_avx512, marker='o', label='-O3 -ipo -xCORE-AVX512')
plt.plot(resolutions, mflops_O3_xcore_avx512, marker='o', label='-O3 -xCORE-AVX512')
plt.plot(resolutions, mflops_O3_fno_alias, marker='o', label='-O3 -fno-alias')

plt.title('MFLOPS Performance Trends for Different Optimization Flags')
plt.xlabel('Resolution')
plt.ylabel('MFLOPS')
plt.xticks(resolutions)  # Ensuring x-axis only shows the given resolutions
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('mflops_trends_optimization_flags.png')


