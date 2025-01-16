import numpy as np
import matplotlib.pyplot as plt

P1 = np.linspace(0, 9, 500)
P2 = (18 - 2 * P1) / 3
		
# Gráfico
plt.figure(figsize=(8, 6))
plt.plot(P1, P2, label=r'$2P_1 + 3P_2 \leq 18$', color='blue')
		
# Ejes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
		
# Región factible
plt.fill_between(P1, 0, P2, where=(P2 >= 0), color='lightblue', alpha=0.5)
		
plt.title('Región Factible: Producción de Modelos 3D y Texturas')
plt.xlabel('Modelos 3D (P1)')
plt.ylabel('Texturas (P2)')
plt.xlim(0, 9)
plt.ylim(0, 6)
plt.legend()
plt.grid()
plt.show()