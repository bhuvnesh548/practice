import pandas as pd
series=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print (series)
df=pd.read_csv("data.csv")
df.info()
print(df)