#11

import openpyxl as o

book=o.open('11 Банк.xlsx',read_only=True)
List=book.active
#print(int((List[2][2].value).year))
for i in range(1,List.max_row+1):
    if List[i][1].value=='Омск' and (1970<int((List[i][2].value).year)<1979):print(List[i][0].value)

