
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


# In[27]:


df_plants_csv = pd.read_csv('simple_dataframe.csv',delimiter ="|")
df_plants_csv


# In[31]:


table = pa.Table.from_pandas(df_plants_csv)
pq.write_table(table, 'plants.parquet')


# In[30]:


df_plants_parquet = pq.read_table('plants.parquet').to_pandas()
# Only read a subset of the columns
#
df_plants_parquet


# In[29]:


df_plants_parquet_filtered = pq.read_table('plants.parquet', columns=['tipo', 'nombre_comun']).to_pandas()
df_plants_parquet_filtered

from fastparquet import write
write('C:\carlos\plants.parq', df)

write('C:\carlos\plants2.parq', df2, row_group_offsets=[0, 1, 2],
      compression='GZIP', file_scheme='hive')

from fastparquet import ParquetFile
pf = ParquetFile('plants2.parq')
df = pf.to_pandas()
df
