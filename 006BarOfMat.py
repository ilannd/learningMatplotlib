import matplotlib.pyplot as plt
import numpy as np

# 12个柱，向上的12个，向下的12个
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n) * np.random.uniform(0.5, 1.0, n))  # uniform为均匀分布
Y2 = (1 - X / float(n) * np.random.uniform(0.5, 1.0, n))
# 向上的柱状图
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
# 向下的柱状图，Y2的值是负的
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    # ha:horizontal alignment(水平对齐方式)
    plt.text(x, y + 0.1, '%.2f' % y, ha='center', va='bottom')
for x, y in zip(X, Y2):
    # va:vertical alignment，，这里要-0.1而且y也要变成负的
    plt.text(x, -y - 0.1, '-%.2f' % y, ha='center', va='top')


plt.xlim(-.5, n)
# 把刻度抹掉了
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()
