# https://matplotlib.org/stable/gallery/spines/multiple_yaxis_with_spines.html

import matplotlib.pyplot as plt


fig, ax = plt.subplots()
fig.subplots_adjust(right=0.75)

twin1 = ax.twinx()
twin2 = ax.twinx()

# Offset the right spine of twin2.  The ticks and label have already been
# placed on the right by twinx above.
twin2.spines['right'].set_position(('axes', 1.2))

p1 = ax.scatter([0, 0.4, 0.8, 1, 1.3, 1.8, 2], [0, 8, 2, 1, 21, 14, 22], c='b', label='Density')
p2 = twin1.scatter([0, 0.7, 0.9, 1, 1.2, 1.5, 2], [0, 34, 23, 23, 12, 8, 16], c='r', label='Temperature')
p3 = twin2.scatter([0, 0.6, 0.8, 1, 1.4, 1.8, 2], [22, 50, 23, 24, 95, 30, 15], c='g', label='Velocity')

ax.set_xlim(0, 2)
ax.set_ylim(0, 30)
twin1.set_ylim(0, 40)
twin2.set_ylim(1, 100)

ax.set_xlabel('Distance')
ax.set_ylabel('Density')
twin1.set_ylabel('Temperature')
twin2.set_ylabel('Velocity')

ax.legend(handles=[p1, p2, p3])

plt.show()