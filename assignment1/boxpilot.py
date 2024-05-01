import matplotlib.pyplot as plt
import pandas as pd

login_data = pd.DataFrame({
    "500": [1802.30, 1819.63, 1766.30, 1880.15, 1492.80, 1582.62],
    "1500": [914.55, 1048.40, 870.37, 969.99, 964.65, 883.61],
    "2500": [739.96, 740.18, 739.19, 730.63, 729.39, 691.00],
    "3500": [676.47, 674.42, 566.68, 673.07, 511.78, 677.65],
    "4500": [678.62, 672.42, 657.99, 532.14, 493.24, 675.39]
}, index=["test1", "test2", "test3", "test4", "test5", "test6"]).astype(float)

batch_data = pd.DataFrame({
    "500": [1237.90, 1287.97, 1256.25, 1294.88, 1330.32, 1293.87],
    "1500": [1082.42, 928.42, 973.03, 1006.14, 1102.31, 954.11],
    "2500": [647.90, 653.98, 646.97, 649.67, 651.51, 648.23],
    "3500": [666.28, 666.48, 665.31, 666.66, 666.50, 667.01],
    "4500": [605.60, 605.15, 605.52, 605.26, 605.75, 604.52]
}, index=["test1", "test2", "test3", "test4", "test5", "test6"]).astype(float)

labels = ['login', 'batch']

plt.figure(figsize=(7, 6))


bplot = plt.boxplot(login_data, patch_artist=True, positions = (1,3,5,7,9), widths=0.6, labels="login")
bplot2 = plt.boxplot(batch_data, patch_artist=True, positions=(1.5,3.5, 5.5, 7.5, 9.5), labels="batch", widths=0.6, boxprops=dict(facecolor="yellow"))
 
plt.title('O3 Login vs Batch FLOPS')
x_position = [1.2, 3.2,5.2,7.2,9.2]
x_position_fmt = ["500", "1500", "2500","3500","4500"]
plt.ylabel('MFLOP/S')
plt.xlabel('Resolution')
plt.xticks([i for i in x_position], x_position_fmt)
plt.legend(handles=[bplot['boxes'][0],bplot2['boxes'][0]], labels=labels)

plt.tight_layout()
plt.savefig('graph_2.pdf')
