import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

# 添加一个3D的axis
ax = Axes3D(fig)

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
# match到底面
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)

# 画3D图
# stride代表步长
# cmap用来映色
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
"""
============= ================================================
        Argument      Description
        ============= ================================================
        *X*, *Y*, *Z* Data values as 2D arrays
        *rstride*     Array row stride (step size), defaults to 10  # 行跨
        *cstride*     Array column stride (step size), defaults to 10  # 列跨
        *color*       Color of the surface patches
        *cmap*        A colormap for the surface patches.
        *facecolors*  Face colors for the individual patches
        *norm*        An instance of Normalize to map values to colors
        *vmin*        Minimum value to map
        *vmax*        Maximum value to map
        *shade*       Whether to shade the facecolors
        ============= ================================================
"""

# I think this is different from contours
# 底面的等高线图
# zdir(zdirection)表示从哪个轴压下去，这里从z轴压下去
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
# ax.contourf(X, Y, Z, zdir='x', offset=-4, cmap=plt.get_cmap('rainbow'))  # 选择投影面x=-4
# ax.contourf(X, Y, Z, zdir='y', offset=4, cmap=plt.get_cmap('rainbow'))
"""
==========  ================================================
        Argument    Description
        ==========  ================================================
        *X*, *Y*,   Data values as numpy.arrays
        *Z*
        *zdir*      The direction to use: x, y or z (default)
        *offset*    If specified plot a projection of the filled contour  # 选择投影面在z=-2
                    on this position in plane normal to zdir
        ==========  ================================================
"""

ax.set_zlim(-2, 2)

plt.show()
