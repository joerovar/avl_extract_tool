import pandas as pd
import datetime
import numpy as np

df_main = pd.read_csv('route20_stop_time_dwell.csv')
df_no_dwell = pd.read_csv('route20_stop_time.csv')

df_no_dwell = df_no_dwell[['schd_trip_id', 'stop_id', 'stop_sequence', 'arrival_time', 'schd_sec', 'event_time']]
df_main = df_main.merge(df_no_dwell, left_on=['trip_id', 'stop_sequence', 'event_time'],
                        right_on=['schd_trip_id', 'stop_sequence', 'event_time'])
df_main.to_csv('route20_stop_time_final.csv', index=False)
