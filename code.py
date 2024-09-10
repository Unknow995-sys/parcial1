# hay que instalar esto: pip install matplotlib numpy
import numpy as np
import matplotlib.pyplot as plt
# Definir las restricciones del problema
def restriccion1(x):
    return (36 - 3 * x) / 2
def restriccion2(x):
    return (18 - x) / 2
# Rango de valores para x
# Se establece un rango para las variables (x_1) (cajas de kesseliana)
x = np.linspace(0, 15, 400)
# Creamos la figura y los ejes
plt.figure(figsize=(10, 8))
# Graficamos las restricciones
plt.plot(x, restriccion1(x), label=r'$3x_1 + 2x_2 \leq 36$', color='blue')
plt.plot(x, restriccion2(x), label=r'$x_1 + 2x_2 \leq 18$', color='red')
plt.axhline(8, color='green', label=r'$x_2 \leq 8$', linestyle='--')
# Llenamos la región factible
plt.fill_between(x, np.minimum(restriccion1(x), restriccion2(x)), 0, where=(np.minimum(restriccion1(x), restriccion2(x)) >= 0) & (8 >= np.minimum(restriccion1(x), restriccion2(x))), color='gray', alpha=0.5)
# Configuramos los ejes
plt.xlim(0, 15)
plt.ylim(0, 10)
plt.xlabel(r'Cajas de Kesseliana $x_1$')
plt.ylabel(r'Cajas de Kyber $x_2$')
plt.title('Región Factible para el Transporte de Mercancías')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
#espero que me haya quedado bien 😖
