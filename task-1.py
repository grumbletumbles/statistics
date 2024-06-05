import numpy as np
import matplotlib.pyplot as plt


def get_data():
    data = []
    for line in open('data', 'r'):
        line = line.strip()
        data.append(float(line))
    return data


data = get_data()
num_bins = int(np.log2(len(data)) + 1)
counts, bin_edges = np.histogram(data, num_bins)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
print("Группированный статистический ряд:")
for center, count in zip(bin_centers, counts):
    print(f"Значение: {center:.2f}, Частота: {count}")

cdf = np.cumsum(counts) / sum(counts)

plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1)
plt.hist(data, bins=num_bins, alpha=0.7, label='Гистограмма')
plt.title('Гистограмма распределения')
plt.xlabel('Значение')
plt.ylabel('Частота')

plt.subplot(1, 2, 2)
plt.step(bin_edges[1:], cdf, where='post', label='CDF')
plt.title('Выборочная функция распределения')
plt.xlabel('Значение')
plt.ylabel('F(x)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

sample_mean = np.mean(data)
sample_variance = np.var(data, ddof=1)

print(f"Выборочное среднее значение: {sample_mean:.2f}")
print(f"Выборочная дисперсия: {sample_variance:.2f}")
