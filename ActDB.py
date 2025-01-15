import pandas as pd
import pyodbc
import csv

# Leer el archivo CSV actualizado
ruta_csv = r'C:\Users\Usuario\Desktop\Auto.P\Walmart_Sales.csv'
df = pd.read_csv(ruta_csv)

# Conectar a la base de datos SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-Q0M1776;'
    'DATABASE=Automat_DB;'
    'UID=sa;'
    'PWD=gabdas'
)

# Crear un cursor
cursor = conn.cursor()

# Verificar e insertar solo las filas nuevas
for index, row in df.iterrows():
    # Verificar si la fila ya existe en la base de datos
    cursor.execute(
        "SELECT COUNT(*) FROM dbo.Walmart_Sales WHERE Store = ? AND Date = ?",
        row['Store'], row['Date']
    )
    count = cursor.fetchone()[0]
    
    # Si la fila no existe, insertarla
    if count == 0:
        cursor.execute(
            "INSERT INTO dbo.Walmart_Sales (Store, Date, Weekly_Sales, Holiday_Flag, Temperature, Fuel_Price, CPI, Unemployment) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            row['Store'], row['Date'], row['Weekly_Sales'], row['Holiday_Flag'], row['Temperature'], row['Fuel_Price'], row['CPI'], row['Unemployment']
        )

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()


