import pandas as pd

def run_etl():
    # 1. Extract
    # Carga de Archivo 
    try:
        df = pd.read_csv('data/citas_clinica.csv')
    except FileNotFoundError:
        print("Error: No se encontró el archivo en data/citas_clinica.csv")
        return

    # 2. Transform
    
    # 'paciente' a Title Case
    df['paciente'] = df['paciente'].str.title()
    
    # 'especialidad' a UPPER
    df['especialidad'] = df['especialidad'].str.upper()

    # 3. Fechas
    # Convierte a datetime.
    df['fecha_cita'] = pd.to_datetime(df['fecha_cita'], errors='coerce')
    
    # Filtra fechas
    df = df.dropna(subset=['fecha_cita'])

    # Reglas de negocio
    # Mantiene solo estado "CONFIRMADA"
    df = df[df['estado'] == 'CONFIRMADA']
    
    # Mantener solo costos mayores a 0
    df = df[df['costo'] > 0]

    # 4. Valores nulos
    # Reemplaza teléfono nulo por "NO REGISTRA"
    df['telefono'] = df['telefono'].fillna('NO REGISTRA')

    # 5. Archivo
    # Guarda el resultado en la ruta
    df.to_csv('data/output.csv', index=False)
    print("ETL completado con éxito. Archivo guardado en data/output.csv")


if __name__ == "__main__":
    run_etl()
