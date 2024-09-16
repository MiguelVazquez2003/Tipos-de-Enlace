import streamlit as st
from datos import electronegatividades , elementos_metalicos
from info_general import mostrar_informacion_general

# Mostrar la información general sobre los tipos de enlaces químicos y la descripción del programa
mostrar_informacion_general(st)

def calcular_enlace(elemento1, elemento2):
    if elemento1 not in electronegatividades or elemento2 not in electronegatividades:
        st.error("Elemento no encontrado en la tabla de electronegatividades.")
        return None

    en1 = electronegatividades[elemento1]
    en2 = electronegatividades[elemento2]
    diferencia = abs(en1 - en2)

    if elemento1 in elementos_metalicos and elemento2 in elementos_metalicos:
        tipo_enlace = "Metálico"
    elif diferencia > 1.7:
        tipo_enlace = "Iónico"
    elif diferencia <= 0.4:
        tipo_enlace = "Covalente no polar"
    else:
        tipo_enlace = "Covalente polar"

    return tipo_enlace

# Mostrar la imagen de la tabla periódica
st.write("### Tabla Periódica")
st.image("tabla_periodica.png", caption="Tabla Periódica de los Elementos", use_column_width=True)

# Crear la interfaz de usuario con Streamlit
st.header("🔍 ¡Identifica el enlace químico! 🧪")
st.write("Ingrese dos elementos químicos para determinar el tipo de enlace.")

# Lista de elementos para el selector
elementos = list(electronegatividades.keys())
elementos.sort()

elemento1 = st.selectbox("Elemento 1:", elementos)
st.write(f"Electronegatividad de {elemento1}: {electronegatividades[elemento1]}")

elemento2 = st.selectbox("Elemento 2:", elementos)
st.write(f"Electronegatividad de {elemento2}: {electronegatividades[elemento2]}")

if st.button("Calcular Enlace"):
    tipo_enlace = calcular_enlace(elemento1, elemento2)
    if tipo_enlace:
        st.success(f"El enlace entre {elemento1} y {elemento2} es {tipo_enlace}")

# Mostrar la imagen de la tabla periódica
st.write("### Tabla Periódica")
st.image("electronegatividad.jpg", caption="Tabla Periódica de los Elementos", use_column_width=True)
