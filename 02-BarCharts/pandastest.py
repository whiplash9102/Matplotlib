import pandas as pd
from matplotlib import pyplot as plt
width = 0.25

df = pd.read_csv('data.csv')
df['LanguagesWorkedWith'] = df['LanguagesWorkedWith'].str.split(';')

df = df.explode('LanguagesWorkedWith')

# Get top 15
top_15 = df['LanguagesWorkedWith'].value_counts().head(15)

# Plot
plt.style.use('fivethirtyeight')
plt.barh(top_15.index, top_15.values, width)

# Add labels
plt.title('Top 15 Most Popular Programming Languages')
plt.xlabel('Number of Developers')

# Make layout nice
plt.tight_layout()
plt.show()