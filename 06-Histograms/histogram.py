import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('/Users/phamthanh/code/matplotlib/06-Histograms/data.csv')
ids = data['Responder_id']
ages = data['Age']
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins = bins, edgecolor = 'black', log = True)

median_age = int(data['Age'].median())

# color = '#fc4f30'
plt.axvline(median_age, color = 'red', label = 'Age Median',
            linewidth = 1)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()