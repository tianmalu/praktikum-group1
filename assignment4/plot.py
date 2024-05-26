import pandas as pd
import matplotlib.pyplot as plt


# Load the data
data = {
    '0': [5248.8, 5121.4], 
    '1': [3248.7, 4940.3],
    '2': [6548.0, 9616.2],
    '4': [12193.2, 18520.7],
    '8': [20741.3, 26519.9],
    '12': [22642.4, 30052.0],
    '16': [23635.5, 31123.9],
    '24': [28282.2, 30433.2],
    '32': [61087.4, 30094.4],
    '48': [66037.9, 25678.5]
}
df = pd.DataFrame(data)

# Calculate speedup
speedup_2000 = df.loc[0]  / df.loc[0, '0']
speedup_6000 =  df.loc[1]/  df.loc[1, '0']

print("Speedup for 2000:")
print(speedup_2000)
print("\nSpeedup for 6000:")
print(speedup_6000)


df = pd.read_csv('flops.csv')

# Extract thread counts and speedup values
threads = df.columns[1:].astype(int) 
speedup_2000 = df.iloc[2, 1:]  
speedup_6000 = df.iloc[3, 1:]  

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup_2000, marker='o', label='Resolution: 2000')
plt.plot(threads, speedup_6000, marker='o', label='Resolution: 6000')

# Add data labels
for i, txt in enumerate(speedup_2000):
    plt.text(threads[i], speedup_2000.iloc[i] - 0.2, str(txt), ha='center', va='top', color='black')
for i, txt in enumerate(speedup_6000):
    plt.text(threads[i], speedup_6000.iloc[i] + 0.2, str(txt), ha='center', va='bottom', color='red')

plt.xticks(threads)
plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('Number of Threads')
plt.ylabel('Speedup')
plt.legend()

# Save the plot
plt.savefig('speedup.png')