import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
data = pd.read_csv('data.csv')


ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

#create a figure for only one subplot
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(ages, dev_salaries, linestyle = '--', color = 'black', label = 'All devs')
ax2.plot(ages, js_salaries, label = 'JavaScript')
ax2.plot(ages, py_salaries, label = 'Python Salaries')

ax1.set_title("Median Salary by Age")
ax1.set_xlabel('Ages')
ax1.set_ylabel('Salaries')

ax1.legend()
fig1.savefig('fig1.png')
plt.tight_layout()
plt.show()