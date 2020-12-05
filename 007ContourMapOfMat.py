import matplotlib.pyplot as plt
import numpy as np


# contour为等高线

# 定义高度函数
def f(x, y):
    # the height function
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
# x,y绑定成网格的输入值
# mesh为网格的意思，grid也是网格的意思
X, Y = np.meshgrid(x, y)

# use plt.contourf to filling contours
# X,Y and value for (X,Y) point
# 8 代表分成10部分,因为0代表最少分为2部分
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)  # 对应的颜色 # 可以是hot和cool

# use plt.contour to add contour lines
# 画等高线
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)

# adding label
# inline=Ture表示画在线里面，就和上一节线把刻度label盖住了一样显示的
# inline=False表示画在线外面,给盖住了，不好看
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())

plt.show()
