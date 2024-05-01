import matplotlib.pyplot as plt
import pandas as pd

login_time = pd.read_csv('login_time.csv')
batch_time = pd.read_csv('batch_time.csv')
login_FLOPS = pd.read_csv('login_FLOPS.csv')
batch_FLOPS = pd.read_csv('batch_FLOPS.csv')
without_ivdep_FLOPS = pd.read_csv('login_without_ivdep.csv')
without_ivdep_and_options_FLOPS = pd.read_csv('login_without_ivdep_and_options.csv')
graph_1 = pd.read_csv('graph_1.csv')
# graph_2 = pd.read_csv('graph_2.csv')

x_values = [500,1500,2500,3500,4500]

plt.figure(figsize=(20, 12)) 


for index, row in graph_1.iterrows():
    if row.iloc[0] == 'initial':
        continue 
    plt.plot(x_values, row.iloc[1:], label=row.iloc[0], marker='x')

plt.title('FLOPS Over Resolution')
plt.xlabel('Resolution')
plt.ylabel('MFLOP/S')
plt.legend()  
plt.grid(True)  

plt.savefig('graph_1_no_initial.pdf')