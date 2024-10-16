import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Generar datos de ejemplo
df = pd.DataFrame({
    'Fecha': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Valor': pd.Series(range(100)) + pd.Series(range(100)).apply(lambda x: x * 0.5)
})

# Configurar título en Streamlit
st.title('Gráfica de líneas simple')

# Mostrar DataFrame en la app
st.write("Datos de ejemplo", df)

# Crear una figura de Matplotlib
fig, ax = plt.subplots()
ax.plot(df['Fecha'], df['Valor'], label='Valor diario')

# Añadir etiquetas y título
ax.set_xlabel('Fecha')
ax.set_ylabel('Valor')
ax.set_title('Gráfico de valores por fecha')

# Mostrar leyenda
ax.legend()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)