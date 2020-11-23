import tkinter as tk
from tkinter import colorchooser, ttk, messagebox
from PIL import ImageTk, Image
from functools import partial
from Prueba_filedialog import buscarArchivo
from Excel import lectura
from Visualizacion import visualizar

colorPers = ['#FCFDBF', '#F66C5C', '#B4367A', '#5D187F', '#221150']
colorSelection = "Magma"


def colorChange():
    global colorSelection, colorPers
    colorSelection = "Personalizado"
    combo.current(4)
    for i in range(0, 5):
        colorPers[i] = colorButtoms[i]['bg']


def color():
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")
    print(color_code)
    return color_code[1]


def setBG(button):
    col = color()
    button['bg'] = col
    if("frame2" in str(button)):
        colorChange()
    print(colorPers)


def setPath(labelPath):
    labelPath['text'] = buscarArchivo()


FILENAME = 'fondo1.png'
root = tk.Tk()
root.title("Gráfico de Coordenadas Paralelas")
root.resizable(width="false", height="false")
root.iconbitmap('paralIcon.ico')

canvas_width = 600
canvas_height = 500

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# IMAGEN DE FONDO
tk_img = ImageTk.PhotoImage(file=FILENAME)
canvas.create_image(300, 250, image=tk_img)

# quit_button = tk.Button(root, text="Quit", command=root.quit, anchor='w',
#                         width=10, activebackground="#33B5E5")
graphImag = Image.open('graph.jpg')
# The (450, 350) is (height, width)
imag = graphImag.resize((300, 150))
graphImagFinal = ImageTk.PhotoImage(imag)

# quit_button_window = canvas.create_window(10, 10, anchor='nw', window=quit_button)
canvas.create_image(150, 100, image=graphImagFinal, anchor='nw')

# SECCION DE BIENVENIDA
txtBienve = "¡Bienvenidos!\nPronto Visualizaremos el gráfico"
bienv = tk.Label(canvas, width=30, text=txtBienve, fg='black', bg='#CBBC91',
                 font=("Verdana", 14), borderwidth=4, relief="groove")
bienv.pack()
canvas.create_window(canvas_width / 2, 50, window=bienv)

# FRAME PARA ARCHIVO
fileFrame = tk.Frame(canvas, relief="groove")
fileFrame.pack()
filePathLabel = tk.Label(fileFrame, width=50, fg='black', bg='white', borderwidth=2, relief="sunken", anchor="e")
filePathLabel.pack(side='left')
fileButtom = tk.Button(fileFrame, anchor='nw', bg='white', text="Seleccionar Archivo", width=15, relief="sunken")
fileButtom['command'] = partial(setPath, filePathLabel)
fileButtom.pack(side='left')
canvas.create_window(75, 270, window=fileFrame, anchor='nw')

# FRAME PARA COLORES DE VARIABLES
colorFrame = tk.Frame(canvas, relief="groove")
colorFrame.pack()

msjColVar = tk.Label(colorFrame, width=29, text="Escala de colores para las variables",
                     fg='black', bg='#CBBC91', borderwidth=4, relief="groove")
msjColVar.pack(side='top')

color1Buttom = tk.Button(colorFrame, anchor='nw', bg='#FCFDBF', width=2, relief="sunken")
color1Buttom['command'] = partial(setBG, color1Buttom)
color1Buttom.pack(side='left')
color2Buttom = tk.Button(colorFrame, anchor='nw', bg='#F66C5C', width=2, relief="sunken")
color2Buttom['command'] = partial(setBG, color2Buttom)
color2Buttom.pack(side='left')
color3Buttom = tk.Button(colorFrame, anchor='nw', bg='#B4367A', width=2, relief="sunken")
color3Buttom['command'] = partial(setBG, color3Buttom)
color3Buttom.pack(side='left')
color4Buttom = tk.Button(colorFrame, anchor='nw', bg='#5D187F', width=2, relief="sunken")
color4Buttom['command'] = partial(setBG, color4Buttom)
color4Buttom.pack(side='left')
color5Buttom = tk.Button(colorFrame, anchor='nw', bg='#221150', width=2, relief="sunken")
color5Buttom['command'] = partial(setBG, color5Buttom)
color5Buttom.pack(side='left')

colorButtoms = [color1Buttom, color2Buttom, color3Buttom, color4Buttom, color5Buttom]
colorScaleMagma = ['#FCFDBF', '#F66C5C', '#B4367A', '#5D187F', '#221150']
colorScaleSolar = ['#331317', '#872F20', '#BC6F13', '#D9C02C', '#E0FD4A']
colorScaleThermal = ['#032333', '#5D3E99', '#C16479', '#FBAD3C', '#E7FA5A']
colorScaleHaline = ['#29186B', '#125F8E', '#419D85', '#9FD55B', '#FDEE99']


def comboSelect(eventObject):
    global colorSelection, colorPers
    select = combo.current()
    print("Nuevo elemento seleccionado:", select)
    if select == 0:
        colors = colorScaleMagma
        colorSelection = "Magma"
    elif select == 1:
        colors = colorScaleSolar

        colorSelection = "Solar"
    elif select == 2:
        colors = colorScaleThermal

        colorSelection = "Thermal"
    elif select == 3:
        colors = colorScaleHaline

        colorSelection = "Haline"
    else:
        colors = colorPers

        colorSelection = "Personalizado"
    for i in range(0, 5):
        colorButtoms[i]['bg'] = colors[i]


def callback(eventObject):
    print(eventObject)


combo = ttk.Combobox(colorFrame, state="readonly", width=12)
combo["values"] = ["Magma", "Solar", "Thermal", "Haline", "Personalizado"]
combo.current(0)
combo.bind("<<ComboboxSelected>>", comboSelect)
combo.pack(side="left")

canvas.create_window(90, 315, window=colorFrame, anchor='nw')

# FRAME PARA COLOR DE COLUMNAS
columColFrame = tk.Frame(canvas, relief="groove")
columColFrame.pack()

columCol1Buttom = tk.Button(columColFrame, anchor='nw', bg='black', width=8, relief="sunken")
columCol1Buttom['command'] = partial(setBG, columCol1Buttom)
columCol1Buttom.pack(side='right')


msjColVar = tk.Label(columColFrame, width=20, text="Color de los ejes",
                     fg='black', bg='#CBBC91', borderwidth=4, relief="groove")
msjColVar.pack(side='left')
canvas.create_window(310, 313, window=columColFrame, anchor='nw')

# # WIDTH FRAMES
# widthFrame = tk.Frame(canvas, relief="groove")
# msjWidth = tk.Label(widthFrame, width=22, text="Ancho de las lineas",
#                     fg='black', bg='#CBBC91', borderwidth=4, relief="groove")
# msjWidth.pack(side='top')

# # COLUMN WIDTH
# widthColFrame = tk.Frame(widthFrame, relief="groove")
# widthColFrame.pack()

# MODES = [
#     ("Grosor 1", 1),
#     ("Grosor 2", 2),
#     ("Grosor 3", 3),
#     # ("Grosor 4", "4"),
# ]

# colVar = tk.IntVar()
# colVar.set(1)  # initialize
# msjColWidth = tk.Label(widthColFrame, width=10, text="Columnas",
#                        fg='black', bg='#CBBC91', borderwidth=4, relief="groove")
# msjColWidth.pack(side='top')
# colWidthList = []
# for text, mode in MODES:
#     b = tk.Radiobutton(widthColFrame, text=text, variable=colVar, value=mode, indicatoron=0, width=10)
#     colWidthList.append(b)
#     b.pack(anchor='w')
# widthColFrame.pack(side='left')

# # VAR WIDTH
# widthVarFrame = tk.Frame(widthFrame, relief="groove")
# widthVarFrame.pack()

# MODES = [
#     ("Grosor 1", 1),
#     ("Grosor 2", 2),
#     ("Grosor 3", 3),
#     # ("Grosor 4", "4"),
# ]

# varVar = tk.IntVar()
# varVar.set(1)  # initialize
# msjVarWidth = tk.Label(widthVarFrame, width=10, text="Variables",
#                        fg='black', bg='#CBBC91', borderwidth=4, relief="groove")
# msjVarWidth.pack(side='top')
# varWidthList = []
# for text, mode in MODES:
#     b = tk.Radiobutton(widthVarFrame, text=text, variable=varVar, value=mode, indicatoron=0, width=10)
#     varWidthList.append(b)
#     b.pack(anchor='w')
# widthColFrame.pack(side='right')

# canvas.create_window(340, 315, window=widthFrame, anchor='nw')

# CHECKBOX FRAME NORMALIZAR DATOS
checkFrame = tk.Frame(canvas, relief="groove")
checkFrame.pack()
nor = tk.IntVar()
normalizar = tk.Checkbutton(checkFrame, text="¿Normalizar los datos numéricos?", variable=nor,
                            relief='groove', borderwidth=4, width=26, bg='#CBBC91', activebackground='#CBBC91').pack()
canvas.create_window(310, 337, window=checkFrame, anchor='nw')


# GENERAR VISUALIZACION FRAME


def generarVis():
    if filePathLabel.cget("text") == '' :
        tk.messagebox.showwarning(message="¡Parece que no has seleccionado un archivo!", title="Error de Archivo")

    else:
        dicc = {"FilePath": filePathLabel.cget("text"),
                "ColColor": columCol1Buttom.cget('bg'),
                "VarColor": colorPers,
                "ScaleNam": colorSelection,
                #"ColWidth": colVar.get(),
                #"VarWidth": varVar.get(),
                "Normaliz": nor.get()
                }
        print(dicc)
        dataSet = lectura(dicc["FilePath"])
        visualizar(dataSet, dicc)


generarFrame = tk.Frame(canvas)
generarButtom = tk.Button(generarFrame, text='¡Generar!', font=("Verdana", 14), relief='groove', 
    borderwidth=4,width=13, height=1,fg='black', bg='#CBBC91')
generarButtom['command'] = partial(generarVis)
generarButtom.pack()
generarFrame.pack()
canvas.create_window(220, 400, window=generarFrame, anchor='nw')

root.mainloop()
