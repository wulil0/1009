import pandas as pd

# 创建一个示例数据帧
data = {'a': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'B', 'C', 'C']}
data = pd.read_excel('test.xlsx')
df = pd.DataFrame(data)

# 使用 groupby 和 transform 来计算频次并进行排序
df['frequency'] = df.groupby('a')['a'].transform('count')
sorted_df = df.sort_values(
    by=['frequency', 'a'], ascending=[False, True])

# 输出排序后的数据帧
print(sorted_df)

# 输出原始数据帧
original_data = df.drop(columns=['frequency'])
# print(original_data)
