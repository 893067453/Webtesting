import xlrd
from xlutils.copy import copy



# xls的文件格式：97-2003
class ReadExcel(object):
    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            self.excel_path = '../excel/register_keyword.xls'
            self.index = 0
        else:
            self.excel_path = excel_path
            self.index = index
        self.data = xlrd.open_workbook(self.excel_path, formatting_info=True,
                                       encoding_override="utf-8")  # 打开Excel文件，获取对象
        self.table = self.data.sheets()[0]  # 获取第一个sheet的数据

    # 获取某行的值
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows is not None:
            for i in range(rows):
                col = self.table.row_values(i)  # 返回该行的所有单元格数据组成的列表
                if '' not in col:
                    result.append(col)
            return result
        return None

    # 获取Excel的行数
    def get_lines(self):
        rows = self.table.nrows  # 获取有效行数
        if rows >= 1:
            return rows
        else:
            return None

    # 获取单元格的值
    def get_cell(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        else:
            return None

    # 写入数据
    def write_data(self, row, col, value):
        read_data = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_data)
        write_data.get_sheet(self.index).write(row, col, value)
        write_data.save('../excel/register_keyword.xls')
        write_data.save(self.excel_path)


if __name__ == "__main__":
    re = ReadExcel()
    print(re.get_data())
    # print(re.get_lines())
    # print(re.get_cell(0, 0))
    # re.write_data(0, 0, 111)




