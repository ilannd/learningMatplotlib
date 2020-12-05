import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)  # 产生从-1到1的等差数列，就是从-1到1分成50等份，num为元素个数，默认50个,这里也定义为50个
y1 = 2 * x + 1
y2 = x ** 2

# 设置坐标轴的取值范围，xlim=xlimit
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# 设置x,y轴的标签
plt.xlabel('I am x')
plt.ylabel('I am y')

# 设置坐标轴的角标
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)

# y轴的角标变成了文字
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])
# 生成好看的字体，r表示正则表达式形式,空格要用\转置，alpha也要用\转置

'''plt.plot(x, y2, label='up')
plt.plot(x, y1, label='down', color='red', linewidth=1.0, linestyle='--')  # color默认颜色为蓝色
# 默认图例，我的默认图例显示在figure的左上角
plt.legend()
'''

'''l1, = plt.plot(x, y2, label='up')  # plt.plot()是有返回值的，但matplotlib里面别忘了加一个逗号
l2, = plt.plot(x, y1, label='down', color='red', linewidth=1.0, linestyle='--')
plt.legend(handles=[l1, l2], labels=['aaa', 'bbb'], loc='best')
# 参数labels就替换了原来的label
# loc参数可以取upper right(右上角),lower right,,,,best(自己选取空间较大的位置)
'''

# 只打印第一个的图例
l1, = plt.plot(x, y2, label='up')  # plt.plot()是有返回值的，但matplotlib里面别忘了加一个逗号
l2, = plt.plot(x, y1, label='down', color='red', linewidth=1.0, linestyle='--')
plt.legend(handles=[l1, ], labels=['aaa', ], loc='best')

plt.show()
