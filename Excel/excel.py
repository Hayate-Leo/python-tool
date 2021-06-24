import openpyxl as opx


class Excel:
    def __init__(self, path):
        self.path = path
        self.read()
        self.execute()
        self.write()
    
    def execute(self):
        list_value = self.get_list_2d(2, 3)
        self.write_list_2d(list_value, 2, 10)

    def read(self):
        self.wb = opx.load_workbook(self.path)
        self.ws = self.wb.worksheets[0]

    def get_value_list(self, t_2d):
        return([[cell.value for cell in row] for row in t_2d])
    
    def get_list_2d(self, start_row, start_col, end_row=False, end_col=False):
        return self.get_value_list(self.ws.iter_rows(min_row=start_row,
                                                    max_row=end_row,
                                                    min_col=start_col,
                                                    max_col=end_col))

    def write_list_2d(self, l_2d, start_row, start_col):
        for y, row in enumerate(l_2d):
            for x, cell in enumerate(row):
                self.ws.cell(row=start_row + y,
                                column=start_col + x,
                                value=l_2d[y][x])

    def write(self):
        self.wb.save(self.path)
    

if __name__ == '__main__':
    Excel('Excel/sample.xlsx')