from EjemploBuscador import ejemplohtml
from Excel import lectura
from ejemploSea import sea
from Prueba_filedialog import buscarArchivo
from Visualizacion import visualizar

if __name__ == '__main__':
    dataSet = lectura((buscarArchivo()))
    visualizar(dataSet)
