from tkinter import Tk 
from tkinter.filedialog import askopenfilename


def buscarArchivo():
	Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
	filename = askopenfilename(filetypes=[("Excel files", "*.xlsx .xls .csv")]) # show an "Open" dialog box and return the path to the selected file
	return filename
