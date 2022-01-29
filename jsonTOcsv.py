import pandas as pd
print('Espere...')
df = pd.read_json (r'lista.json')
df.to_csv (r'lista.csv', index = None)
print('Listo')
