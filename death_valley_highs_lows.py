from datetime import datetime
import matplotlib.pyplot as plt

import csv

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # load TMAX, TMIN, DATE
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            high_c = 5/9 * (high - 32)
            low = int(row[5])
            low_c = 5/9 * (low - 32)
        except ValueError:
            print("Missing data for {}".format(current_date))
        else:
            dates.append(current_date)
            highs.append(high_c)
            lows.append(low_c)


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title('Highest and lowest daily temperature\nDeath Valley 2018', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (C)', fontsize=15)
ax.tick_params(axis='both', which='major', labelsize=15)

plt.savefig('TMAX_TLOW_Death_Valley.png', bbox_inches='tight')
plt.show()
