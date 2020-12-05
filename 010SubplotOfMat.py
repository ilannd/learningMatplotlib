import matplotlib.pyplot as plt

# example 1:
###############################
plt.figure(figsize=(6, 4))

# plt.subplot(n_rows, n_cols, plot_num)
# 将figure分成两行两列，且在第一个位置plot一个东西
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 2])

plt.subplot(2, 2, 3)  # 写成223也能识别
plt.plot([0, 1], [0, 3])

plt.subplot(2, 2, 4)
plt.plot([0, 1], [0, 4])
# tight_layout会自动调整子图参数，使之填充整个图像区域。这是个实验特性，可能在一些情况下不工作。它仅仅检查坐标轴标签、刻度标签以及标题的部分。
plt.tight_layout()

# example 2:
###############################
plt.figure(figsize=(6, 4))
# plt.subplot(n_rows, n_cols, plot_num)
plt.subplot(2, 1, 1)
# figure splits into 2 rows, 1 col, plot to the 1st sub-fig
plt.plot([0, 1], [0, 1])

plt.subplot(234)  # 注意这里是3，，注意这里是4，不是2
# figure splits into 2 rows, 3 col, plot to the 4th sub-fig
plt.plot([0, 1], [0, 2])

plt.subplot(235)
# figure splits into 2 rows, 3 col, plot to the 5th sub-fig
plt.plot([0, 1], [0, 3])

plt.subplot(236)
# figure splits into 2 rows, 3 col, plot to the 6th sub-fig
plt.plot([0, 1], [0, 4])

plt.tight_layout()
plt.show()
