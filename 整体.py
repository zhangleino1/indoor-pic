import matplotlib.pyplot as plt
import matplotlib

# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimSun'] 
matplotlib.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False 


# 示例数据（请替换为您的实际数据）
locations = ['Loc1', 'Loc2', 'Loc3', 'Loc4', 'Loc5']
cnn_acc = [0.85, 0.88, 0.82, 0.90, 0.87]
scm_acc = [0.80, 0.83, 0.78, 0.85, 0.82]
knn_acc = [0.75, 0.78, 0.72, 0.80, 0.79]
cnn_transformer_acc = [0.88, 0.90, 0.85, 0.92, 0.89]

# 绘制不同方法的准确度
plt.plot(locations, cnn_acc, marker='o', label='CNN')
plt.plot(locations, scm_acc, marker='s', label='SVM')
plt.plot(locations, knn_acc, marker='^', label='KNN')
plt.plot(locations, cnn_transformer_acc, marker='d', label='CNN+Transformer')

# 图表细节
plt.xlabel('Location')
plt.ylabel('Accuracy')
plt.title('不同位置的准确度比较')
plt.legend()
plt.ylim(0, 1)
plt.grid(True)

# 显示图形
plt.show()
