import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

# Read data
data = pd.read_csv('/Users/phamthanh/code/matplotlib/07-ScatterPlot/data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

# Use seaborn styling
plt.style.use('seaborn-v0_8')

# Create scatter plot
plt.scatter(view_count, likes, c=ratio, cmap='summer',
            edgecolors='black', alpha=0.7, linewidths=1)

# Add colorbar for ratio
cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')


#Log the chart
plt.xscale('log')
plt.yscale('log')

# Axis labels and title
plt.xlabel('Number of Views')
plt.ylabel('Number of Likes')
plt.title('Video Correlation between Views and Likes/Dislikes')

# Improve layout and show plot
plt.tight_layout()
plt.show()
