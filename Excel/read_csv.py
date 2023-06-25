import pandas as pd
from tkinter import filedialog
import openpyxl as opx


def read_filepathes() -> tuple:
    typ = [('CSV，テキストファイル', '*.csv; *.txt')]
    dir = r'C:'
    return filedialog.askopenfilenames(filetypes=typ, initialdir=dir)
 

def read_csv(pathes):
    dfs = [pd.read_csv(path, header=0, encoding='utf-8') for path in pathes]
    return dfs
 

def write_excel(dfs, excel_name, pathes):
    wb = opx.Workbook()
    wb.save('data/'+excel_name+'.xlsx')
    with pd.ExcelWriter('data/'+excel_name+'.xlsx', engine='openpyxl', mode='a') as writer:
        for df, path in zip(dfs, pathes):
            df.to_excel(writer, index=False, sheet_name=path.split('/')[-1].replace('.csv', ''))

if __name__ == '__main__':
    # Excelファイル名
    excel_name = '230429_person_info'
    pathes = read_filepathes()
    print(pathes)
    # dfs = read_csv(pathes)
    # write_excel(dfs, excel_name, pathes)
