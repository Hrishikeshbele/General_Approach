'''
save pandas dataframe to to different sheets in excel.
'''

# when you are saving first sheet

writer = pd.ExcelWriter("Duplicate_Heat_id.xlsx", engine = 'openpyxl')
duplicates.to_excel(writer, sheet_name = 'HM_Anal_Duplicates',index=False)
writer.save()
writer.close()

#when you wish to "append" data on the same excel file but another sheet

# saving duplicates to different sheet of file 
from openpyxl import load_workbook
book = load_workbook("Duplicate_Heat_id.xlsx")
writer = pd.ExcelWriter("Duplicate_Heat_id.xlsx", engine = 'openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
duplicates.to_excel(writer, sheet_name = 'Steel_Anal_Duplicates',index=False)
writer.save()
writer.close()
