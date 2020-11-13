import xlrd

def lectura():
    loc = ('/Users/anagu/OneDrive/Documentos/TEC/SemestreII2020/VD/Proyecto2/datos.xls')

    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    # For row 0 and column 0
    #print(sheet.cell_value(0, 0))
    dataDicc = {}
    for col in range(sheet.ncols):
        print(sheet.cell_value(0,col))
        ejeName = (sheet.cell_value(0,col))
        dataSet = []
        for row in range(1,sheet.nrows):
            dataSet.append(sheet.cell_value(row,col))
        dataDicc[ejeName] = dataSet

        print(dataDicc[ejeName])

