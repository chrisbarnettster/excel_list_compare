def compare_lists(dfold,dfnew,columnold='User ID',columnnew='User ID', filtercolumn='Role', filterexpr='Student'):
    # filter by column (only students)
    dfold_students = dfold[dfold[filtercolumn]==filterexpr]
    dfnew_students = dfnew[dfnew[filtercolumn]==filterexpr]
    listold = list(dfold_students[columnold])
    listnew = list(dfnew_students[columnnew])
    intersection = set(listnew).intersection(set(listold))
    #difference = list(set(listnew) - set(listold))
    return intersection



import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

oldfile = "CEM1000W_2018_2019_03_07.xlsx"
newfile = "CEM1000W_2019_2019_03_07.xlsx"
oldsheet = 'Sheet0'
newsheet = 'Sheet0'

dfold = pd.read_excel(oldfile, sheet_name=oldsheet)
dfnew = pd.read_excel(newfile, sheet_name=newsheet)


print(dfold.columns)

#Assume column names the same...
for key in dfold.columns:
   tmpl = compare_lists(dfold,dfnew, key, key)
   print(len(tmpl),sorted(tmpl))
