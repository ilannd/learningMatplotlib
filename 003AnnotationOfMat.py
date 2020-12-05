import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)  # 产生从-1到1的等差数列，就是从-1到1分成50等份，num为元素个数，默认50个,这里也定义为50个
y1 = 2 * x + 1

plt.figure(num=1, figsize=(8, 5))
plt.plot(x, y1)

ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2 * x0 + 1
# 用散点图绘制哪一个点
plt.scatter(x0, y0, s=50, color='b')  # s表示size,,,b表示blue
plt.plot([x0, x0], [0, y0], 'k--', lw=2.5)
# 用两个点绘制一条直线，k--是简写，表示color=‘k’黑色，linestyle='--',lw是linewidth的缩写

# method1 of Annotation
# xy是一个坐标，表示从哪一个点开始打印这个annotation
# xycoords表示xy这个坐标以data的值作为一个基准
# xytext表示基于xy这个点，横坐标+30，纵坐标-30
# offset points偏移点，textcoords表示基于xy这个点
# arrowprops表示那个线和箭头，，connectionstyle表示弧度
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

# method2 of Annotation
# -3,3表示text 的开始坐标，sigma_i中的_i表示下标
plt.text(-3, 3, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$', fontdict={'size': 16, 'color': 'r'})


plt.show()
