import numpy as np
import matplotlib.pyplot as plt

p = np.poly1d([1, 0, 2, 0, 0, 1])
d1 = p.deriv(1)
d2 = p.deriv(2)

print(f"x = 2, fx = {p(2)}", end='\n\n')
print(f"x = 5, fx = {p(5)}", end='\n\n')
print(f"f'x:\n{d1}", end='\n\n')
print(f"f''x:\n{d2}", end='\n\n')

x = np.linspace(-10, 10, 100)
plt.figure(figsize=(8, 8))


def setup_centered_axis(ax, title):
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.set_title(title)


ax1 = plt.subplot(3, 1, 1)
setup_centered_axis(ax1, 'Polynomial')
ax1.plot(x, p(x), 'r-')

ax2 = plt.subplot(3, 1, 2)
setup_centered_axis(ax2, 'First Derivative')
ax2.plot(x, d1(x), 'b--')

ax3 = plt.subplot(3, 1, 3)
setup_centered_axis(ax3, 'Second Derivative')
ax3.plot(x, d2(x), 'go')

plt.tight_layout()
plt.show()
