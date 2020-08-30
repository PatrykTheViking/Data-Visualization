import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # load TMAX
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        high_c = 5/9 * (high - 32)
        dates.append(current_date)
        highs.append(high_c)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

ax.set_title('Highest daily temperature - 2018', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (C)', fontsize=15)
ax.tick_params(axis='both', which='major', labelsize=15)

plt.savefig('TMAX.png', bbox_inches='tight')
plt.show()