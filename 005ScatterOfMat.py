import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
# random.normal(loc=0,scale=1e-2,size=shape)表示正态分布
# 正态分布的均值loc对应着分布的中心，正态分布的标准差scale（越大越矮胖，越小越瘦高）
# size(int整数或者整数数组)对应输出矩阵的shape
Y = np.random.normal(0, 1, n)
# T 表示颜色值
T = np.arctan2(Y, X)  # for color value
plt.scatter(X, Y, s=75, c=T, alpha=0.5)    # s表示size,为散点的大小,c表示color
# plt.scatter(np.arange(5), np.arange(5))
plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))
'''# 刻度给的值为空元祖，刻度就没了
plt.xticks(())
plt.yticks(())
'''
plt.show()
