import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 500)
y = (50 - 5 * x) / 10
		
# Gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$5x + 10y \leq 50$', color='blue')
		 
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
		
# Región factible
plt.fill_between(x, 0, y, where=(y >= 0), color='lightblue', alpha=0.5)
		
plt.title('Región Factible: Producción de Dispositivos')
plt.xlabel('Dispositivos Tipo A (x)')
plt.ylabel('Dispositivos Tipo B (y)')
plt.xlim(0, 10)
plt.ylim(0, 5)
plt.legend()
plt.grid()
plt.show()