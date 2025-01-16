
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 12, 500)
y = 12 - x
x_min = 4
y_min = 6	
# Gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$x + y \leq 12$', color='blue')
plt.axvline(x_min, color='green', linestyle='--', label=r'$x \geq 4$')
plt.axhline(y_min, color='orange', linestyle='--', label=r'$y \geq 6$')
		
# Región factible
plt.fill_between(x, y_min, y, where=(x >= x_min) & (y >= y_min), color='lightblue', alpha=0.5)
		
plt.title('Región Factible: Tiempo de Reuniones y Documentación')
plt.xlabel('Reuniones (x)')
plt.ylabel('Documentación (y)')
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.legend()
plt.grid()
plt.show()