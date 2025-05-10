import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from sklearn.manifold import TSNE
import seaborn as sns
from matplotlib.ticker import MultipleLocator

# Set up the figure with two subplots
plt.figure(figsize=(15, 6))

# Create data for the t-SNE plot
# Generate some sample data for 5 different clusters
np.random.seed(42)

# Create some sample clusters with different positions
def generate_cluster(center, size, scale=10):
    return center + np.random.randn(size, 2) * scale

# Generate 5 distinct clusters with different positions
cluster1 = generate_cluster([-50, -50], 20, scale=10)  # Red cluster (bottom left)
cluster2 = generate_cluster([0, 40], 20, scale=10)     # Purple cluster (middle left)
cluster3 = generate_cluster([30, 0], 10, scale=5)      # Green cluster (center)
cluster4 = generate_cluster([80, 0], 20, scale=10)     # Orange cluster (right)
cluster5 = generate_cluster([30, 80], 20, scale=10)    # Blue cluster (top)

# Combine all clusters
X = np.vstack([cluster1, cluster2, cluster3, cluster4, cluster5])
labels = np.hstack([
    np.zeros(20),   # For cluster 1
    np.ones(20),    # For cluster 2
    np.ones(10)*2,  # For cluster 3
    np.ones(20)*3,  # For cluster 4
    np.ones(20)*4   # For cluster 5
])

# First subplot: t-SNE visualization
plt.subplot(1, 2, 1)

# Define colors for each cluster
colors = ['red', 'purple', 'green', 'orange', 'blue']
clusters = [cluster1, cluster2, cluster3, cluster4, cluster5]

# Plot each cluster with its corresponding color
for i, (cluster, color) in enumerate(zip(clusters, colors)):
    plt.scatter(cluster[:, 0], cluster[:, 1], color=color, s=50)

plt.xlim(-75, 125)
plt.ylim(-75, 125)
plt.title('(a) t-SNE map', fontsize=12)
plt.xlabel('', fontsize=10)
plt.ylabel('', fontsize=10)

# Second subplot: Localization Performance bar chart
plt.subplot(1, 2, 2)
models = ['CNN', 'LSTM', 'CViTLoc']
errors = [65.0, 6.4, 2.46]

# Create the bar chart
bars = plt.bar(models, errors, width=0.6, color='white', edgecolor='black', hatch='//')

# Add the values on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height}', ha='center', va='bottom', fontsize=12)

plt.ylim(0, 80)
plt.yticks(range(0, 81, 10))
plt.title('(b) Localization Performance', fontsize=12)
plt.ylabel('MLE (in cm)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add figure title
plt.suptitle('Fig. 7. (a) represents t-SNE map for five location embeddings, (b) localization error comparison\nwith baseline model.', 
             fontsize=12, y=-0.05)

plt.tight_layout()
plt.show()