import pandas as pd
import datetime
import numpy as np

df_final = pd.read_csv('route20_stop_time_final.csv')
df_no_dwell = pd.read_csv('route20_stop_time.csv')
cols = df_no_dwell.columns.tolist()
cols += ['dwell_time', 'passenger_load', 'departure_time']
cols.remove('diff')
df_final = df_final[cols]
df_final.to_csv('route20_stop_time_merged.csv', index=False)

