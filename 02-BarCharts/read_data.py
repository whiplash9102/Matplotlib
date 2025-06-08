import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt


plt.xkcd()

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        languages = row['LanguagesWorkedWith'].split(';')
        language_counter.update(languages)


    programming_languages = []
    popularity =[]
    for item in language_counter.most_common(15):
        programming_languages.append(item[0])
        popularity.append(item[1])
    
    popularity.reverse()
    programming_languages.reverse()

    plt.barh(programming_languages, popularity, color = 'red', label= 'All devs')
    plt.title('Most Popular Languages')
    plt.xlabel('Number of people who use')

    plt.legend()
    plt.tight_layout()

    plt.show()