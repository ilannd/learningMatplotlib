import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)  # 产生从-1到1的等差数列，就是从-1到1分成50等份，num为元素个数，默认50个,这里也定义为50个
y1 = 2 * x + 1
y2 = x ** 2

'''# 创建一个画布
plt.figure()
plt.plot(x, y1)'''

# 创建另一个画布
plt.figure(num=3, figsize=(8, 5))  # 能明显看到figure 比上一个要小
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')  # color默认颜色为蓝色

# 设置坐标轴的取值范围，xlim=xlimit
plt.xlim((-1, 2))
plt.ylim((-2, 3))

'''# 设置x,y轴的标签
plt.xlabel('I am x')
plt.ylabel('I am y')'''

# 设置坐标轴的角标
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)

# y轴的角标变成了文字
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])
# 生成好看的字体，r表示正则表达式形式,空格要用\转置，alpha也要用\转置

# gca='get current axis'
# 获取了当前的坐标轴
# ax.spines表示四个坐标轴（边框），包括(left,top,right,bottom)
ax = plt.gca()

# 把上边和右边的轴设置成没有
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 现在还没有设置哪个是X轴，哪个是Y轴
# 设置bottom轴为X轴
ax.xaxis.set_ticks_position('bottom')
# 设置left轴为Y轴
ax.yaxis.set_ticks_position('left')

# 挪动x轴和y轴
# 注意传入的是元组
ax.spines['bottom'].set_position(('data', 0))  # 挪到y轴的0,,,参数不止有data,还有outward,axes,比如('axes',0.1)就是挪到y轴的10%
ax.spines['left'].set_position(('data', 0))   # 挪到x轴的0
plt.show()
