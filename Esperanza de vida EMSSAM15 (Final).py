#================================================
#================================================
#          Andrea Barragan Ongay 205783 
#          CALCULO DE LLA qx EMSSAM-15
#===============================================
#===============================================
import pandas as pd
tabla = pd.read_csv("/Users/andybarragan/Desktop/EMSSAM15.csv")
#===============================================
#===============================================
#Creación de la tabla 
tabla.columns = tabla.columns.str.strip().str.lower()
print("Columnas:", tabla.columns.tolist())
#===============================================
#===============================================
# Inputs
sexo = input("Ingrese el sexo (Hombre/Mujer): ")
if sexo not in ["Hombre", "Mujer"]:
    raise ValueError("Sexo no válido. Escriba 'Hombre' o 'Mujer'.")

edad_inicial = int(input("Ingrese la edad inicial: "))
#===============================================
#===============================================
# Definir columnas de qx según sexo
if sexo == "Hombre":
    qx_col = "qx_hombres"
else:
    qx_col = "qx_mujeres"
#===============================================
#===============================================
# Construcción de la subtabla desde la edad inicial
subtabla = tabla[["edad", qx_col]].copy()
subtabla = subtabla[subtabla["edad"] >= edad_inicial]
subtabla = subtabla.rename(columns={qx_col: "qx"})
#===============================================
#===============================================
#Calculos 
# Calcular px = 1 - qx
subtabla["px"] = 1 - subtabla["qx"]

# Supervivencias acumuladas
supervivencias = []
w = 1
for i in subtabla["px"]:
    w *= i
    supervivencias.append(w)
    
# Columna de supervivencias
subtabla["supervivencia"] = supervivencias


# Esperanza de vida
ex = subtabla["supervivencia"].sum()
#===============================================
#===============================================
print(f"Esperanza de vida a la edad {edad_inicial} para {sexo}: {ex:.2f} años")
#===============================================
#===============================================
