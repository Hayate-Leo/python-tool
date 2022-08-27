from tkinter import filedialog
import os

files = filedialog.askopenfilenames()

for file in files:
    names = file.split('_')
    os.rename(file, names[0]+'-hayateleo-'+names[1])