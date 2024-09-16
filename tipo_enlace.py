import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Diccionario de electronegatividades (completo)
electronegatividades = {
    'H': 2.20, 'He': 0.00, 'Li': 0.98, 'Be': 1.57, 'B': 2.04, 'C': 2.55, 'N': 3.04, 'O': 3.44, 'F': 3.98,
    'Ne': 0.00, 'Na': 0.93, 'Mg': 1.31, 'Al': 1.61, 'Si': 1.90, 'P': 2.19, 'S': 2.58, 'Cl': 3.16, 'Ar': 0.00,
    'K': 0.82, 'Ca': 1.00, 'Sc': 1.36, 'Ti': 1.54, 'V': 1.63, 'Cr': 1.66, 'Mn': 1.55, 'Fe': 1.83, 'Co': 1.88,
    'Ni': 1.91, 'Cu': 1.90, 'Zn': 1.65, 'Ga': 1.81, 'Ge': 2.01, 'As': 2.18, 'Se': 2.55, 'Br': 2.96, 'Kr': 3.00,
    'Rb': 0.82, 'Sr': 0.95, 'Y': 1.22, 'Zr': 1.33, 'Nb': 1.6, 'Mo': 2.16, 'Tc': 1.9, 'Ru': 2.2, 'Rh': 2.28,
    'Pd': 2.20, 'Ag': 1.93, 'Cd': 1.69, 'In': 1.78, 'Sn': 1.96, 'Sb': 2.05, 'Te': 2.1, 'I': 2.66, 'Xe': 2.6,
    'Cs': 0.79, 'Ba': 0.89, 'La': 1.10, 'Ce': 1.12, 'Pr': 1.13, 'Nd': 1.14, 'Pm': 1.13, 'Sm': 1.17, 'Eu': 1.2,
    'Gd': 1.2, 'Tb': 1.1, 'Dy': 1.22, 'Ho': 1.23, 'Er': 1.24, 'Tm': 1.25, 'Yb': 1.1, 'Lu': 1.27, 'Hf': 1.3,
    'Ta': 1.5, 'W': 2.36, 'Re': 1.9, 'Os': 2.2, 'Ir': 2.20, 'Pt': 2.28, 'Au': 2.54, 'Hg': 2.00, 'Tl': 1.62,
    'Pb': 2.33, 'Bi': 2.02, 'Po': 2.0, 'At': 2.2, 'Rn': 0.0, 'Fr': 0.7, 'Ra': 0.9, 'Ac': 1.1, 'Th': 1.3,
    'Pa': 1.5, 'U': 1.38, 'Np': 1.36, 'Pu': 1.28, 'Am': 1.3, 'Cm': 1.3, 'Bk': 1.3, 'Cf': 1.3, 'Es': 1.3,
    'Fm': 1.3, 'Md': 1.3, 'No': 1.3, 'Lr': 1.3, 'Rf': 1.3, 'Db': 1.3, 'Sg': 1.3, 'Bh': 1.3, 'Hs': 1.3,
    'Mt': 1.3, 'Ds': 1.3, 'Rg': 1.3, 'Cn': 1.3, 'Nh': 1.3, 'Fl': 1.3, 'Mc': 1.3, 'Lv': 1.3, 'Ts': 1.3, 'Og': 1.3
}

# Diccionario de nombres completos de los elementos (completo)
nombres_completos = {
    'H': 'Hidrógeno', 'He': 'Helio', 'Li': 'Litio', 'Be': 'Berilio', 'B': 'Boro', 'C': 'Carbono', 'N': 'Nitrógeno', 'O': 'Oxígeno', 'F': 'Flúor',
    'Ne': 'Neón', 'Na': 'Sodio', 'Mg': 'Magnesio', 'Al': 'Aluminio', 'Si': 'Silicio', 'P': 'Fósforo', 'S': 'Azufre', 'Cl': 'Cloro', 'Ar': 'Argón',
    'K': 'Potasio', 'Ca': 'Calcio', 'Sc': 'Escandio', 'Ti': 'Titanio', 'V': 'Vanadio', 'Cr': 'Cromo', 'Mn': 'Manganeso', 'Fe': 'Hierro', 'Co': 'Cobalto',
    'Ni': 'Níquel', 'Cu': 'Cobre', 'Zn': 'Zinc', 'Ga': 'Galio', 'Ge': 'Germanio', 'As': 'Arsénico', 'Se': 'Selenio', 'Br': 'Bromo', 'Kr': 'Kriptón',
    'Rb': 'Rubidio', 'Sr': 'Estroncio', 'Y': 'Itrio', 'Zr': 'Circonio', 'Nb': 'Niobio', 'Mo': 'Molibdeno', 'Tc': 'Tecnecio', 'Ru': 'Rutenio', 'Rh': 'Rodio',
    'Pd': 'Paladio', 'Ag': 'Plata', 'Cd': 'Cadmio', 'In': 'Indio', 'Sn': 'Estaño', 'Sb': 'Antimonio', 'Te': 'Telurio', 'I': 'Yodo', 'Xe': 'Xenón',
    'Cs': 'Cesio', 'Ba': 'Bario', 'La': 'Lantano', 'Ce': 'Cerio', 'Pr': 'Praseodimio', 'Nd': 'Neodimio', 'Pm': 'Prometio', 'Sm': 'Samario', 'Eu': 'Europio',
    'Gd': 'Gadolinio', 'Tb': 'Terbio', 'Dy': 'Disprosio', 'Ho': 'Holmio', 'Er': 'Erbio', 'Tm': 'Tulio', 'Yb': 'Iterbio', 'Lu': 'Lutecio', 'Hf': 'Hafnio',
    'Ta': 'Tantalio', 'W': 'Wolframio', 'Re': 'Renio', 'Os': 'Osmio', 'Ir': 'Iridio', 'Pt': 'Platino', 'Au': 'Oro', 'Hg': 'Mercurio', 'Tl': 'Talio',
    'Pb': 'Plomo', 'Bi': 'Bismuto', 'Po': 'Polonio', 'At': 'Astato', 'Rn': 'Radón', 'Fr': 'Francio', 'Ra': 'Radio', 'Ac': 'Actinio', 'Th': 'Torio',
    'Pa': 'Protactinio', 'U': 'Uranio', 'Np': 'Neptunio', 'Pu': 'Plutonio', 'Am': 'Americio', 'Cm': 'Curio', 'Bk': 'Berkelio', 'Cf': 'Californio', 'Es': 'Einstenio',
    'Fm': 'Fermio', 'Md': 'Mendelevio', 'No': 'Nobelio', 'Lr': 'Lawrencio', 'Rf': 'Rutherfordio', 'Db': 'Dubnio', 'Sg': 'Seaborgio', 'Bh': 'Bohrio', 'Hs': 'Hassio',
    'Mt': 'Meitnerio', 'Ds': 'Darmstadtio', 'Rg': 'Roentgenio', 'Cn': 'Copernicio', 'Nh': 'Nihonio', 'Fl': 'Flerovio', 'Mc': 'Moscovio', 'Lv': 'Livermorio', 'Ts': 'Tenesino', 'Og': 'Oganesón'
}

# Lista de elementos metálicos (más completa)
elementos_metalicos = [
    'Li', 'Be', 'Na', 'Mg', 'Al', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 
    'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Cs', 'Ba', 'La', 'Ce', 
    'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 
    'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 
    'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 
    'Mc', 'Lv', 'Ts', 'Og'
]

def calcular_enlace():
    elemento1 = entrada1.get().capitalize()
    elemento2 = entrada2.get().capitalize()

    if elemento1 not in electronegatividades or elemento2 not in electronegatividades:
        messagebox.showerror("Error", "Elemento no encontrado en la tabla de electronegatividades.")
        return

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

    resultado.config(text=f"El enlace entre {elemento1} y {elemento2} es {tipo_enlace}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Enlaces Químicos")

# Crear y colocar los widgets
titulo = tk.Label(ventana, text="Calculadora de Enlaces Químicos", font=("Helvetica", 16, "bold"))
titulo.grid(row=0, columnspan=2, pady=10)

descripcion = tk.Label(ventana, text="Ingrese dos elementos químicos para determinar el tipo de enlace.", font=("Helvetica", 10))
descripcion.grid(row=1, columnspan=2, pady=5)

tk.Label(ventana, text="Elemento 1:", font=("Helvetica", 10)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entrada1 = tk.Entry(ventana, font=("Helvetica", 10))
entrada1.grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Label(ventana, text="Elemento 2:", font=("Helvetica", 10)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
entrada2 = tk.Entry(ventana, font=("Helvetica", 10))
entrada2.grid(row=3, column=1, padx=10, pady=5, sticky="w")

boton = tk.Button(ventana, text="Calcular Enlace", command=calcular_enlace, font=("Helvetica", 10, "bold"), bg="#4CAF50", fg="white")
boton.grid(row=4, columnspan=2, pady=10)

resultado = tk.Label(ventana, text="", font=("Helvetica", 12))
resultado.grid(row=5, columnspan=2, pady=10)

# Crear un marco para la tabla
frame_tabla = tk.Frame(ventana)
frame_tabla.grid(row=6, columnspan=2, pady=10)

# Crear la tabla de electronegatividades
tabla = ttk.Treeview(frame_tabla, columns=("Elemento", "Nombre", "Electronegatividad"), show='headings')
tabla.heading("Elemento", text="Elemento")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Electronegatividad", text="Electronegatividad")

# Insertar datos en la tabla
for elemento, en in electronegatividades.items():
    nombre_completo = nombres_completos[elemento]
    tabla.insert("", "end", values=(elemento, nombre_completo, en))

# Estilo para la tabla
estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
estilo.configure("Treeview", font=("Helvetica", 10), rowheight=25)

tabla.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()