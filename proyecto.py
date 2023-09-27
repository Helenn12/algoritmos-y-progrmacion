#Vamos a crear un diccionario de fornulas quimicas para facilitar algunos elementos de la tabla periodica
#Se deben crear un diccionario completamente diferente en cada elemento 
#Cada diccionario debe estar cerrado y ser completamente unico

# Diccionario de fórmulas químicas

formulas_quimicas = {
    "Hidrógeno": {
        "Nombre": "Hidrógeno",
        "Símbolo": "H",
        "Número atómico": 1,
        "Fórmula química": "H2"
    },
    "Lantano": {
        "Nombre": "Lantano",
        "Símbolo": "La",
        "Número atómico": 57,
        "Fórmula química": "La2O3"
    },
    "Tántalo": {
        "Nombre": "Tántalo",
        "Símbolo": "Ta",
        "Número atómico": 73,
        "Fórmula química": "Ta2O5"
    },
    "Renio": {
        "Nombre": "Renio",
        "Símbolo": "Re",
        "Número atómico": 75,
        "Fórmula química": "NH4Re04"
    },
    "Osmio": {
        "Nombre": "Osmio",
        "Símbolo": "Os",
        "Número atómico": 76,
        "Fórmula química": "OsO4"
    },
    "Iridio": {
        "Nombre": "Iridio",
        "Símbolo": "Ir",
        "Número atómico": 77,
        "Fórmula química": "IrO2"
    },
    "Platino": {
        "Nombre": "Platino",
        "Símbolo": "Pt",
        "Número atómico": 78,
        "Fórmula química": "Pt"
    },
    "Paladio": {
        "Nombre": "Paladio",
        "Símbolo": "Pd",
        "Número atómico": 46,
        "Fórmula química": "Pd"
    },
    "Estaño": {
        "Nombre": "Estaño",
        "Símbolo": "Sn",
        "Número atómico": 50,
        "Fórmula química": "SnO2"
    },
    "Telurio": {
        "Nombre": "Telurio",
        "Símbolo": "Te",
        "Número atómico": 52,
        "Fórmula química": "Te"
    }
}

# Bucle interactivo para buscar elementos
while True:
    elemento = input("Introduce el nombre del elemento (o 'salir' para finalizar): ")
    if elemento.lower() == 'salir':
        break
    if elemento in formulas_quimicas:
        informacion_elemento = formulas_quimicas[elemento]
        print(f"Información del elemento {elemento}:")
        for clave, valor in informacion_elemento.items():
            print(f"{clave}: {valor}")
    else:
        print("Elemento no encontrado. Por favor, verifica el nombre del elemento.")

