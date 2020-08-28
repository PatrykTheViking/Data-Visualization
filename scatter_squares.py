import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.PuBuGn, s=10)
# ax.plot(x_values, y_values, linewidth=1)

"""define chart label and label names"""
ax.set_title("Squares", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square values", fontsize=14)

"""define label size"""
# ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plt.show()
# plt.savefig('scatter_squares.png', bbox_inches='tight') - optional for a direct save
