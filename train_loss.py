import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像时负号'-'显示为方块的问题

# 创建数据
epochs = np.linspace(0, 150, 300)

# 创建平滑曲线的函数
def smooth_curve(x, y):
    x_new = np.linspace(min(x), max(x), 300)
    spl = make_interp_spline(x, y, k=3)
    y_new = spl(x_new)
    return x_new, y_new

# 过滤CSI的损失数据（红色实线）
# 从初始值快速下降到接近0
filtered_loss = np.zeros_like(epochs)
# 初始高点
filtered_loss[:10] = np.exp(-np.linspace(0, 3, 10)) * 6
# 接近0后保持低值
filtered_loss[10:] = 0.1 * np.exp(-np.linspace(0, 3, 290)) + 0.02

# 原始CSI的损失数据（蓝色虚线）
# 从初始值缓慢下降
original_loss = np.zeros_like(epochs)
# 初始高点
original_loss[:10] = np.exp(-np.linspace(0, 2, 10)) * 8
# 缓慢下降
original_loss[10:100] = np.exp(-np.linspace(0, 2, 90)) * 3 + 0.3
# 继续缓慢下降直到接近0
original_loss[100:] = np.exp(-np.linspace(0, 2, 200)) * 0.3 + 0.05

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制两条曲线
plt.plot(epochs, filtered_loss, 'r-', linewidth=2, label='Loss with Filtered CSI')
plt.plot(epochs, original_loss, 'b-.', linewidth=2, label='Loss with Original CSI')

# 添加标记点和标注
plt.annotate('0.021', xy=(50, 0.5), xytext=(50, 1.2),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             fontsize=12, ha='center')

plt.annotate('0.070', xy=(140, 0.12), xytext=(140, 1.2),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             fontsize=12, ha='center')

# 设置图表属性
plt.grid(True)
plt.xlabel('Epoch index', fontsize=14)
plt.ylabel('Loss', fontsize=14)
plt.ylim(0, 9)
plt.xlim(0, 150)
plt.legend(fontsize=12)
plt.title('Figure 8. The training loss values using different CSI datasets.', fontsize=14, pad=20, loc='center', y=-0.15)

# 设置图表样式
plt.tight_layout()

# 显示图表
plt.show()