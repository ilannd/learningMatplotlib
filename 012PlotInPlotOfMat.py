import matplotlib.pyplot as plt

fig = plt.figure()

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# below are all percentage,相对于整个figure的百分比
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8

ax1 = fig.add_axes([left, bottom, width, height])  # main axes
# 绘图区域为整个figure的左边10%开始，下边10%开始，height变为原figure的height的80%，width变为原figure的width的80%
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

ax2 = fig.add_axes([0.2, 0.6, 0.25, 0.25])  # inside axes
ax2.plot(y, x, 'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')


# different method to add axes
####################################
plt.axes([0.6, 0.2, 0.25, 0.25])
# y[::-1]将y的值逆序一下
plt.plot(y[::-1], x, 'g')
# 不用ax.set_xlabel(),直接plt.xlabel()
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()