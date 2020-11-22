import plotly.graph_objects as go


# Funcion encargada de generar los diccionarios de valores a visualizar
def visualizar(dataSet):
    datos = []                                                              # Lista de datos a graficar
    for item in dataSet:                                                    # Para cada elemento en el dicc dataSet
        if ((str(dataSet[item][0])).isdigit()) or isinstance((dataSet[item][0]), float):   # En caso de que sean números
            dicc = dict(label=item, values=dataSet[item])
        else:                                                               # En caso de que sean nombres
            columna = []                                                    # Elementos existentes
            ubicaciones = []                                                # Ubicación de cada variable segun elemento
            max = 0                                                         # Max de elementos
            for item2 in dataSet[item]:                                   # Para cada elemento en la lista de dicc[item]
                if item2 in columna:                                        # Si el elemento existe, agregue su pos
                    ubicaciones.append(columna.index(item2)+1)
                else:                                                       # Si no, agregue elemento, pos, max ++
                    ubicaciones.append(len(columna)+1)
                    columna.append(item2)
                    max += 1
            dicc = dict(range=[1, max], tickvals=list(range(1, max+1)), label=item,
                        values=ubicaciones, ticktext=columna)
        datos.append(dicc)                                                 # Agregue el elemento a datos
    ejemplohtml(datos)


# Funcion encargada de generar la visualización con los datos correspondientes
def ejemplohtml(datos):
    fig = go.Figure(data=go.Parcoords(line_color='blue', dimensions=datos))

    # NEED FIX
    config = dict({
        'scrollZoom': True,
        'displayModeBar': True,
        'editable': True
    })

    fig.update_layout(
        title={
            'text': "Plot Title",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    fig.show(config=config)
