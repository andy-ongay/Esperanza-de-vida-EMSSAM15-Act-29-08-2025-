# Esperanza-de-vida-EMSSAM15-Act-29-08-2025-
Codigo de calculo de la esperanza de vida con datos del EMSSAM15 
#================================================
#================================================
#          Andrea Barragan Ongay 205783 
#          CALCULO DE LLA qx EMSSAM-15
#===============================================
#===============================================
Nota: Profe, La verdad tengo dudas del codigo, 
lo intente hacer porque me dio curiosidad ver 
como podria funcionar pero nada mas me confundi
mas, como que ya no supe si era correcto el 
concepto que estaba usando 
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
