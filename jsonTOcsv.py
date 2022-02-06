import pandas as pd
#import os
from glob import glob

con = 0
arc = []  
r = 0
print('archivos:\n---------')
archivos = glob('*.json') 
for archivo in archivos:
    arc.append(archivo) 
    con+=1
    print( str(con) + ") " + archivo)

while True:
    print('Ingrese numero: ')
    r = int(input())
    if r >= 1 and r<=con:
        break 

# 
df = pd.read_json (arc[r-1])
df.to_csv (r'convertido_Json_Csv.csv', index = None)
print('\nHecho!!\n')
