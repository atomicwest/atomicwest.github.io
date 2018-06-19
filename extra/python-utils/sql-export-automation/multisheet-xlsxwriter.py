import pandas as pd
import xlsxwriter as xw

df1 = pd.DataFrame({'tst': list(range(10, 20))})
df2 = pd.DataFrame({'tst': list(range(30, 40))})

writer = pd.ExcelWriter('tst.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='mapping')
df2.to_excel(writer, sheet_name='export')

writer.save()
