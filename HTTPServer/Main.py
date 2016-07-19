import xlrd

workbook = xlrd.open_workbook('test.xls')

#print sheets content
for sheet in workbook.sheets():
    for row in range(sheet.nrows):
        for column in range(sheet.ncols):
            if sheet.cell(row,column).value != xlrd.empty_cell:
                print sheet.cell(row,column).value,
        print
    print "\n\n\n"

print '\n'
#name of sheets
for sheet in workbook.sheet_names():
    print sheet