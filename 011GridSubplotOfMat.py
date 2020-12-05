import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec  # 第二种方法需要导入的库

# method 1: subplot2grid
##########################
plt.figure()
# plot出5个axis

# 三行三列，(0,0)原点开始，列跨度为3
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)  # stands for axes
ax1.plot([1, 2], [1, 2])
# 原来是plt.title(),现在是ax.set_title(),xlim等也一样需要改变
ax1.set_title('ax1_title')

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)

ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

# colspan和rowspan默认都是1
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.scatter([1, 2], [2, 2])
# 原来是plt.xlabel(),现在是ax.set_label()
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')

ax5 = plt.subplot2grid((3, 3), (2, 1))

# method 2: gridspec
#########################
plt.figure()
# 三行三列
gs = gridspec.GridSpec(3, 3)
# use index from 0
ax6 = plt.subplot(gs[0, :])  # 第0行，所有列
ax7 = plt.subplot(gs[1, :2])  # 第一行，第0，1列
ax8 = plt.subplot(gs[1:, 2])  # 第1,2行，第2列
ax9 = plt.subplot(gs[-1, 0])  # 第2行，第0列
ax10 = plt.subplot(gs[-1, -2])  # 第2行，第1列

# method 3: easy to define structure
####################################
# 注意这里是plt.subplots()，不是plt.subplot()
# 一个元组代表一行，f代表figure object
# 若需要改figure的格式，用f 来修改
# 四个axis共享x,y轴
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])
plt.tight_layout()


plt.show()
