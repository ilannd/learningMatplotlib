import matplotlib.pyplot as plt
import numpy as np

# 有时候画线会把坐标轴的一些信息遮挡住,需要将被遮挡的刻度的label显示出来

x = np.linspace(-3, 3, 50)  # 产生从-1到1的等差数列，就是从-1到1分成50等份，num为元素个数，默认50个,这里也定义为50个
y1 = 0.1 * x

plt.figure(num=1, figsize=(8, 5))
# zorder:轴的默认绘制顺序是补丁1，线条2，文本3。此顺序由zorder属性确定
plt.plot(x, y1, linewidth=10, zorder=1)
plt.ylim(-2, 2)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)  # 将label变大
    label.set_zorder(2)
    # label(2)在线(1)上
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))
    # bbox就是label后面的框框
    # facecolor表示框框前面的颜色
    # edgecolor表示框框的框的颜色
    # alpha表示透明度,值越小越透明

# 其实按照博主的代码被遮挡的刻度的label是显示不出来的，需要
# 在plt.plot()设置参数zorder=1
# 在label上加上label.set_zorder(2)

plt.show()
