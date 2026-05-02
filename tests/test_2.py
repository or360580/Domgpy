import matplotlib.pyplot as plt
import numpy as np

def generar_grafica_aleatoria(puntos=100):
    """
    Genera una gráfica de caminata aleatoria.
    """
    # 1. Crear datos aleatorios
    x = np.arange(puntos)
    y = np.cumsum(np.random.randn(puntos)) # Suma acumulada para crear una línea continua

    # 2. Configurar la estética de la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Tendencia Aleatoria', color='teal', linewidth=2)
    
    # 3. Añadir detalles
    plt.title("Gráfica de Datos Aleatorios", fontsize=14)
    plt.xlabel("Tiempo / Pasos")
    plt.ylabel("Valor Acumulado")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # 4. Mostrar la gráfica
    plt.show()

if __name__ == "__main__":
    generar_grafica_aleatoria(150)