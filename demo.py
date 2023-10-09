import numpy
import pandas as pd
import numpy as np

path = 'test.xlsx'
newPath = 'new.csv'

f = pd.read_excel(path)
# p = f.sort_values(by=f.columns[0])
num = len(set(f['a']))
print(num)

f['Result'] = None
g = f.groupby('a')

f['Result'] = f['b'].apply(lambda x: 'pass' if x == '=' else 'fail')
h = g.filter(lambda group: len(set(group['Result'])) == 1)


ztsn = 0
passsn = h[h['Result'] == 'pass']
ztsn = len(set(passsn['a']))

print(ztsn)
ztl = ztsn/num
print(ztl)

h[h['Result'] == 'fail'].to_csv(newPath)
# h.to_csv('a.csv')
