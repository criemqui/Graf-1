import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Fijar las calificaciones promedio en los valores proporcionados
calificaciones_fijas = [81.0, 70.0, 77.5]

# Asegurar que los errores sean no negativos
error_inferior_matematicas = max(0, calificaciones_fijas[0] - 71.7)
error_superior_matematicas = 81.5 - calificaciones_fijas[0]

error_inferior_ciencias = max(0, calificaciones_fijas[1] - 66.5)
error_superior_ciencias = max(0, 70.5 - calificaciones_fijas[1])

error_inferior_literatura = max(0, calificaciones_fijas[2] - 76.5)
error_superior_literatura = max(0, 84.5 - calificaciones_fijas[2])

# Errores inferiores y superiores separados
errores = [
    [error_inferior_matematicas, error_inferior_ciencias, error_inferior_literatura],
    [error_superior_matematicas, error_superior_ciencias, error_superior_literatura]
]

# Etiquetas de las materias
materias = ['Matemáticas', 'Ciencias', 'Literatura']

# Crear gráfico de barras de error
fig, ax = plt.subplots()
x = np.arange(len(materias))
width = 0.35

# Barras de calificaciones con barras de error
bars = ax.bar(x, calificaciones_fijas, width, yerr=errores, capsize=10, color='white', edgecolor='white')

# Crear el gráfico
#fig, ax = plt.subplots()

# Añadir barras de error manualmente
for i in range(len(materias)):
    ax.errorbar(x[i], calificaciones_fijas[i], 
                yerr=[[errores[0][i]], [errores[1][i]]], 
                fmt='none',  # No mostrar el marcador aquí
                ecolor='blue',  # Color de la barra de error
                elinewidth=2,  # Ancho de la barra de error
                capsize=10,  # Tamaño del extremo de la barra de error
                capthick=2)  # Grosor del extremo de la barra de error
    
    # Ajustar la posición del punto en la barra de error para literatura
    if materias[i] == 'Literatura':
        punto_y = 80.0  # Establecer el punto en 80.0 para Literatura
    else:
        punto_y = calificaciones_fijas[i] - errores[0][i] / 2  # Ajustar esta línea para mover el punto hacia abajo
    
    ax.plot(x[i], punto_y, 'o', color='blue', markersize=5)  # Tamaño y color del marcador

# Etiquetas, título y leyenda
ax.set_xlabel('Materias')
ax.set_ylabel('Calificaciones Promedio')
ax.set_title('Calificaciones Promedio con barras de Error')
ax.set_xticks(x)
ax.set_xticklabels(materias)

# Ajustar los límites del eje y para que coincidan con los intervalos proporcionados
ax.set_ylim(65, 90)  # Un pequeño margen inferior y superior

# Establecer las etiquetas del eje y con los intervalos proporcionados
yticks = np.arange(67.5, 85.1, 2.5)
ax.set_yticks(yticks)

# Crear entradas de leyenda
error_handle = Line2D([0], [0], color='black', lw=2, linestyle='-', marker='o', 
                      markersize=5, markerfacecolor='blue', label='Promedio')

# Añadir leyenda personalizada sin la entrada 'Promedio'
ax.legend(handles=[error_handle], loc='upper left', bbox_to_anchor=(0, 1.0),
          title="", title_fontsize='large', borderpad=1, labelspacing=1.5, 
          handlelength=3, handleheight=3, handletextpad=2, fontsize='medium', 
          edgecolor='black', facecolor='white', fancybox=True, shadow=True)




# Mostrar gráfico
plt.show()
