import numpy as np
import matplotlib.pyplot as plt

# Generar datos sintéticos
rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Crear el histograma
plt.figure(figsize=(10, 6))
plt.hist(matematicas, bins=10, color='blue', edgecolor='blue', alpha=0.7)

# Personalizar el histograma
plt.title('Distribución de Calificaciones de Matemáticas')
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Frecuencia')
plt.grid(False)  # Desactivar la cuadrícula

# Mostrar el histograma
plt.show()
