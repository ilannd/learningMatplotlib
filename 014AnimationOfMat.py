import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))  # plot()返回值是一个列表


def animate(i):  # 传入第i帧，即第i个时间点
    line.set_ydata(np.sin(x + i / 10.0))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.sin(x))
    return line,


# call the animator.  blit=True means only re-draw the parts that have changed.
# blit=True dose not work on Mac, set blit=False
# interval= update frequency
# frames=100,表示100帧，100个updates
# interval=20，表示updates的频率，隔20毫秒更新一次
# blit=True表示只更新变化了的点，blit=False表示更新整张图片
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init,
                              interval=20, blit=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
