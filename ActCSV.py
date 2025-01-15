import pandas as pd

# Datos de la nueva fila en formato de diccionario
nueva_fila = {
    'Store': 7,
    'Date': '2025-02-14',
    'Weekly_Sales': 13345.67,
    'Holiday_Flag': 0,
    'Temperature': 15.5,
    'Fuel_Price': 3.47,
    'CPI': 220.23,
    'Unemployment': 5.2
}

# Ruta del archivo CSV
ruta_csv = r'C:\Users\Usuario\Desktop\Auto.P\Walmart_Sales.csv'

# Leer el archivo CSV en un DataFrame
df = pd.read_csv(ruta_csv)

# Crear un DataFrame para la nueva fila
df_nueva_fila = pd.DataFrame([nueva_fila])

# Agregar la nueva fila al DataFrame existente usando concat
df_fila_agregada = pd.concat([df, df_nueva_fila], ignore_index=True)

# Guardar el DataFrame actualizado en el archivo CSV
df_fila_agregada.to_csv(ruta_csv, index=False)

