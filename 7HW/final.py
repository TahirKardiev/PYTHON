import pandas as pd
data = pd.read_csv("c:/Users/ANDREY/Desktop/Code/HW/Python/7HW/california_housing_train.csv")
print(data)
# rows = len(data.axes[0])
# cols = len(data.axes[1])
  
# # Print the number of rows and columns
# print("Number of Rows: " + str(rows))
# print("Number of Columns: " + str(cols))

# datatypes = data.dtypes
# print(datatypes)

# print(data.isnull().sum())

df = pd.read_csv("california_housing_train.csv")
# print(df[['subtitle', 'sku']])

# print((df['ribbon'] > 2) & (df['sku']>1))
print(df['sku'].max(), df['sku'].min())

print(df.loc[df['ribbon'].min(), ['showOnFrontpage']].max())