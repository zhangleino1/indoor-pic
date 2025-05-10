import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# 设置绘图风格
plt.style.use('default')
plt.figure(figsize=(10, 7))

# 创建步进式累积分布函数数据
# DeepPos 2 NN (红色实线)
deeppos_errors = [0.2, 0.4, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.8, 4.2, 4.8, 5.2, 5.8]
deeppos_cdf = np.linspace(0.05, 0.95, len(deeppos_errors))

# DeepFi 2 NN (蓝色虚线)
deepfi_errors = [0.8, 1.0, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.2, 2.8, 4.4, 4.9, 5.0]
deepfi_cdf = np.linspace(0.05, 0.95, len(deepfi_errors))

# 创建步进式CDF
def create_step_cdf(x, y):
    x_step = []
    y_step = []
    
    # 添加起点
    x_step.append(0)
    y_step.append(0)
    
    # 构建阶梯状数据
    for i in range(len(x)):
        x_step.append(x[i])
        y_step.append(y[i])
        
        # 如果不是最后一个点，添加一个水平线段点
        if i < len(x) - 1:
            x_step.append(x[i])
            y_step.append(y[i+1])
    
    # 添加终点确保到达最大值
    x_step.append(6)
    y_step.append(1)
    
    return x_step, y_step

# 创建步进式CDF数据
x_deeppos, y_deeppos = create_step_cdf(deeppos_errors, deeppos_cdf)
x_deepfi, y_deepfi = create_step_cdf(deepfi_errors, deepfi_cdf)

# 绘制CDF曲线
plt.plot(x_deeppos, y_deeppos, 'r-', linewidth=2, label='DeepPos 2 NN')
plt.plot(x_deepfi, y_deepfi, 'b:', linewidth=2, label='DeepFi 2 NN')

# 设置图表属性
plt.grid(True)
plt.xlabel('Distance Error(m)', fontsize=12)
plt.ylabel('CDF', fontsize=12)
plt.xlim(0, 6)
plt.ylim(0, 1)
plt.xticks(np.arange(0, 7, 1))
plt.yticks(np.arange(0, 1.1, 0.1))

# 添加图例
plt.legend(loc='lower right', fontsize=11)

# 设置次要网格线
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', alpha=0.5)
plt.grid(which='major', linestyle='-', alpha=0.8)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()