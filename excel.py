import openpyxl
import data
def create_to_excel(wbname, data, sheetname='Sheet1', ):
    print("正在创建excel表格%s......" % (wbname))
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = sheetname

    # 将数据data写入excel表格中;
    print("正在写入数据........")
    for row, item in enumerate(data):  # data发现有4行数据， item里面有三列数据;
        for column, cellValue in enumerate(item):
            cell = sheet.cell( column=row + 1,row=column + 1, value=cellValue)
    wb.save(wbname)
    print("保存工作薄%s成功......." % (wbname))
if __name__ == '__main__':
    data=data.demo()
    create_to_excel('D:\\excel2.xlsx',data,'矩阵')
