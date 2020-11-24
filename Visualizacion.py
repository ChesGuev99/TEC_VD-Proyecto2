import plotly.graph_objects as go
import plotly.express as px

# Esta función se utiliza para la normalización del gráfico
# Se obtiene el menor valor numérico de todos los datos
def obtenerMenorDato(dataSet, mayorDato):
    dato = mayorDato
    for clave in dataSet:
        datos = dataSet[clave]
        for elemento in datos:
            if (type(elemento) == int or type(elemento) == float):
                if (elemento < dato):
                    dato = elemento
    return int(dato)


# Esta función se utiliza para la normalización del gráfico
# Se obtiene el mayor valor numérico de todos los datos
def obtenerMayorDato(dataSet):
    dato = 0
    for clave in dataSet:
        datos = dataSet[clave]
        for elemento in datos:
            if (type(elemento) == int or type(elemento) == float):
                if (elemento > dato):
                    dato = elemento
    return int(dato) + 1


# Esta función obtiene la mayor cantidad de datos de una columna
# Esto para poder asiganarle un color a cada línea en el gráfico
def obtenerCantidadDatos(dataSet):
    cantidad = 0
    for clave in dataSet:
        datos = dataSet[clave]
        if (len(datos) > cantidad):
            cantidad = len(datos)
    return cantidad + 1


# Funcion encargada de generar los diccionarios de valores a visualizar
def visualizar(dataSet, valoresGUI):
    datos = []
    if (valoresGUI["Normaliz"] == 0):  # Verifica que se pida un gráfico normalizado o no
        for item in dataSet:  # Para cada elemento en el dicc dataSet
            if ((str(dataSet[item][0])).isdigit()) or isinstance((dataSet[item][0]),
                                                                 float):  # En caso de que sean números
                dicc = dict(label=item, values=dataSet[item])
            else:  # En caso de que sean nombres
                columna = []  # Elementos existentes
                ubicaciones = []  # Ubicación de cada variable segun elemento
                max = 0  # Max de elementos
                for item2 in dataSet[item]:  # Para cada elemento en la lista de dicc[item]
                    if item2 in columna:  # Si el elemento existe, agregue su pos
                        ubicaciones.append(columna.index(item2) + 1)
                    else:  # Si no, agregue elemento, pos, max ++
                        ubicaciones.append(len(columna) + 1)
                        columna.append(item2)
                        max += 1
                dicc = dict(range=[1, max], tickvals=list(range(1, max + 1)), label=item,
                            values=ubicaciones, ticktext=columna)
            datos.append(dicc)  # Agregue el elemento a datos

    else:  # Se debe hacer con escala normalizada
        mayorDato = obtenerMayorDato(dataSet)  # Se obtiene el mayor valor numérico de todos los datos
        menorDato = obtenerMenorDato(dataSet, mayorDato)  # Se obtiene el menor valor numérico de todos los datos
        for item in dataSet:  # Para cada elemento en el dicc dataSet
            if ((str(dataSet[item][0])).isdigit()) or isinstance((dataSet[item][0]),
                                                                 float):  # En caso de que sean números
                dicc = dict(range=[menorDato, mayorDato], label=item,
                            values=dataSet[item])  # Se le asigna como rango del valor más pequeño al más grande
            else:  # En caso de que sean nombres
                columna = []  # Elementos existentes
                ubicaciones = []  # Ubicación de cada variable segun elemento
                max = 0  # Max de elementos
                for item2 in dataSet[item]:  # Para cada elemento en la lista de dicc[item]
                    if item2 in columna:  # Si el elemento existe, agregue su pos
                        ubicaciones.append(columna.index(item2) + 1)
                    else:  # Si no, agregue elemento, pos, max ++
                        ubicaciones.append(len(columna) + 1)
                        columna.append(item2)
                        max += 1
                dicc = dict(range=[1, max], tickvals=list(range(1, max + 1)), label=item,
                            values=ubicaciones, ticktext=columna)
            datos.append(dicc)  # Agregue el elemento a datos

    cantDatos = obtenerCantidadDatos(dataSet)
    ejemplohtml(datos, valoresGUI, cantDatos)


# Funcion encargada de generar la visualización con los datos correspondientes
def ejemplohtml(datos, dicc, cantDatos):
    colores = 0
    if dicc["ScaleNam"] != "Personalizado":
        colores = dicc["ScaleNam"]
    else:
        colores = dicc["VarColor"]

    fig = go.Figure(data=go.Parcoords(line_color=list(range(1, cantDatos)),
                                      line_colorscale=colores,
                                      dimensions=datos,
                                      labelfont_color=dicc["ColColor"],
                                      labelfont_size=13,
                                      rangefont_color=dicc["ColColor"],
                                      line_showscale=True))

    # NEED FIX
    config = dict({
        'scrollZoom': True,
    })

    fig.update_layout(
        title={
            'text': "",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    fig.show(config=config)
