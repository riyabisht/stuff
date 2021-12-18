from google.colab import drive
drive.mount('/gdrive')
import pandas as pd
df=pd.read_csv('movies.csv')
df1=df.dropna()
with open('/gdrive/My Drive/foo.csv', 'w') as f:
  df1.to_csv(f)
#df1.to_csv('/drive/My Drive/data/movie1.csv')