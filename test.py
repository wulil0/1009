import numpy
import pandas as pd
import numpy as np

f = pd.read_excel('test.xlsx')
p = f.sort_values(by=['a'])
f['Result'] = None
passn = 0
# print(f)
g = f.groupby('a')
# for key, group in g:
#     print(group)
#     # print(key)
#     # print(len(set(group['b'])))
#     x = len(set(group['b']))

# f.replace('=','pass')
# print(f)
# for column in f.columns:
#     f[column] = f[column].apply(lambda x: 'a' if x =='pass' else 'b')
f['Result'] = f['b'].apply(lambda x: 'pass' if x =='=' else 'fail')
print(f)



h = g.filter(lambda group: len(set(group['Result'])) == 1)
# print(h)
h.to_csv('a.csv')
num = len(set(p['a']))
# print(num)
