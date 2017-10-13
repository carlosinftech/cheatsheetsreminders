
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


# In[27]:


df_plants_csv = pd.read_csv('C:\carlos\simple_dataframe.csv',delimiter ="|")
df_plants_csv


# In[31]:


table = pa.Table.from_pandas(df_plants_csv)
pq.write_table(table, 'C:\carlos\plants.parquet')


# In[30]:


df_plants_parquet = pq.read_table('C:\carlos\plants.parquet').to_pandas()
# Only read a subset of the columns
#
df_plants_parquet


# In[29]:


df_plants_parquet_filtered = pq.read_table('C:\carlos\plants.parquet', columns=['tipo', 'nombre_comun']).to_pandas()
df_plants_parquet_filtered
