from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd

plt.style.use('fivethirtyeight')

languages_counter = Counter()
data = pd.read_csv('/Users/phamthanh/code/matplotlib/02-BarCharts/data.csv')
lang_response = data['LanguagesWorkedWith']

for response in lang_response:
    languages_counter.update(response.split(';'))

languages = []
popularity = []

for item in languages_counter.most_common(5):
    languages.append(item[0])
    popularity.append(item[1])

color = ['#0b132b','#1c2541', '#3a506b', '#5bc0be', '#ff6b6b' ]
explode = [0, 0, 0, 0.1, 0]

patches, texts, autotexts = plt.pie(
    popularity, labels=languages, colors=color,
    explode=explode, wedgeprops={'edgecolor': 'black'},
    shadow=True, startangle=90, autopct='%1.1f%%'
)

for autotext in autotexts:
    autotext.set_color('white')  # 👈 Set percentage text color to white

plt.title('Super Pie')

plt.tight_layout()
plt.show()
