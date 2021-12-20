import pandas as pd
import numpy as np

df = pd.read_csv('route20_stop_time_merged.csv')
df = df[['route_id','trip_id','stop_id','stop_sequence','schd_time','schd_sec','avl_arr_time','avl_sec','avl_dep_time','avl_dep_sec','dwell_time','passenger_load','ron','fon','roff','foff']]
df.to_csv('route20_stop_time_merged.csv', index=False)
#
# print(df.dtypes)
# print(df2.dtypes)
