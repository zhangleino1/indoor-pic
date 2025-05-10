import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Set the font properties for better visualization
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# Create a figure with 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Data for the plots
# (a) Loss vs Layers
layers = [2, 4, 8, 12]
loss_layers = [2800, 2700, 2700, 3200]

# (b) Loss vs Batch Size
batch_sizes = [128, 256, 512, 1024]
loss_batch = [3200, 3100, 2700, 2800]

# (c) CNN kernel size
kernel_sizes = [2, 5, 10, 15]
loss_kernel = [3900, 2200, 2700, 2600]

# (d) Number of filters
filter_nums = [128, 160, 192, 224, 512]
loss_filters = [3000, 2600, 1800, 1200, 800]

# Plot (a): Loss vs Layers
axs[0, 0].bar(range(len(layers)), loss_layers, color='navy', edgecolor='black', hatch='/')
axs[0, 0].set_xticks(range(len(layers)))
axs[0, 0].set_xticklabels(layers)
axs[0, 0].set_xlabel('No. of Transformer Layers')
axs[0, 0].set_ylabel('MSE')
axs[0, 0].set_ylim(0, 4000)
axs[0, 0].yaxis.set_major_locator(MultipleLocator(1000))
axs[0, 0].grid(axis='y', linestyle='--', alpha=0.7)
axs[0, 0].set_title('(a) Loss vs Layers')

# Plot (b): Loss vs Batch Size
axs[0, 1].bar(range(len(batch_sizes)), loss_batch, color='darkorange', edgecolor='black', hatch='\\')
axs[0, 1].set_xticks(range(len(batch_sizes)))
axs[0, 1].set_xticklabels(batch_sizes)
axs[0, 1].set_xlabel('Batch Size')
axs[0, 1].set_ylabel('MSE')
axs[0, 1].set_ylim(0, 4000)
axs[0, 1].yaxis.set_major_locator(MultipleLocator(1000))
axs[0, 1].grid(axis='y', linestyle='--', alpha=0.7)
axs[0, 1].set_title('(b) Loss vs Batch Size')

# Plot (c): CNN kernel size
axs[1, 0].bar(range(len(kernel_sizes)), loss_kernel, color='forestgreen', edgecolor='black', hatch='/')
axs[1, 0].set_xticks(range(len(kernel_sizes)))
axs[1, 0].set_xticklabels(kernel_sizes)
axs[1, 0].set_xlabel('Kernel Size (r)')
axs[1, 0].set_ylabel('MSE')
axs[1, 0].set_ylim(0, 4000)
axs[1, 0].yaxis.set_major_locator(MultipleLocator(1000))
axs[1, 0].grid(axis='y', linestyle='--', alpha=0.7)
axs[1, 0].set_title('(c) CNN kernel size')

# Plot (d): Number of filter
axs[1, 1].bar(range(len(filter_nums)), loss_filters, color='darkred', edgecolor='black', hatch='/')
axs[1, 1].set_xticks(range(len(filter_nums)))
axs[1, 1].set_xticklabels(filter_nums)
axs[1, 1].set_xlabel('No. of Filters (n)')
axs[1, 1].set_ylabel('MSE')
axs[1, 1].set_ylim(0, 4000)
axs[1, 1].yaxis.set_major_locator(MultipleLocator(1000))
axs[1, 1].grid(axis='y', linestyle='--', alpha=0.7)
axs[1, 1].set_title('(d) Number of filter')

# Add a main title for the entire figure
fig.suptitle('Fig. 6. Model Training Parameters.', fontsize=14, y=0.02)

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(bottom=0.1)

# Show the plot
plt.show()