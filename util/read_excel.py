import xlrd
import os


def get_value_by_row(file_name, sheet, row_num):
    """
    :param file_name: Excel file name
    :rtype: list
    :param sheet: sheet_name or sheet_index(sheet1,sheet2...0,1,2...)
    :param row_num: (0,1,2...)
    :return: list([1,2,3])
    """
    file_name = file_name
    file_dir = os.path.dirname(__file__) + '../../testdata/' + file_name + '.xlsx'
    workbook = xlrd.open_workbook(file_dir)
    if type(sheet) == int:
        table = workbook.sheet_by_index(sheet)
    elif type(sheet) == str:
        table = workbook.sheet_by_name(sheet)
    else:
        table = None
    ncols = table.ncols
    row_values = []
    for col_num in range(ncols):
        col_values = table.cell_value(row_num, col_num)
        row_values.append(col_values)
    return row_values


def get_value_in_order(file_name, sheet):
    """
    :param file_name: file name
    :param sheet: sheet_name or sheet_index(Sheet1,Sheet2.../0,1,2...)
    :return: list[list]  ([[1,2,3],[1,4,2]])
    """
    file_name = file_name
    file_dir = os.path.dirname(__file__) + '../../testdata/' + file_name + '.xlsx'
    workbook = xlrd.open_workbook(file_dir)
    if type(sheet) == int:
        table = workbook.sheet_by_index(sheet)
    elif type(sheet) == str:
        table = workbook.sheet_by_name(sheet)
    else:
        table = None
    nrows = table.nrows
    ncols = table.ncols
    table_values = []
    for row_num in range(1, nrows):
        row_value = []
        for col_num in range(ncols):
            cell_value = table.cell_value(row_num, col_num)
            row_value.append(cell_value)
        table_values.append(row_value)
    return table_values


def test_get_value_by_row():
    file_name = 'testdata'
    sheet = 0
    row_num = 1
    print(get_value_by_row(file_name, sheet, row_num))

def test_get_value_in_order():
    file_name = 'testdata'
    sheet = 0
    print(get_value_in_order(file_name,sheet))


if __name__ == '__main__':
    test_get_value_by_row()
    test_get_value_in_order()
