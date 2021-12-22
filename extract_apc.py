import pandas as pd
import numpy as np

# df = pd.read_csv('route20_stop_time_merged.csv')
# df_trips = pd.read_csv('trips.txt')
# df_trips_rt20 = df_trips[df_trips['route_id'] == str(20)]
# df_trips_rt20.to_csv('trips_route20.txt', index=False)
# df_trips_rt20 = df_trips_rt20[['schd_trip_id', 'block_id']]
# df_trips_rt20['schd_trip_id'] = df_trips_rt20['schd_trip_id'].astype(int)
#
# df = df.merge(df_trips_rt20, left_on='trip_id', right_on='schd_trip_id')
# df = df.drop(labels=['bus_id', 'schd_trip_id'], axis=1)
# df.to_csv('route20_stop_time_merged(try).csv', index=False)
df = pd.read_csv('route20_stop_time_merged(try).csv')
print(df.shape[0])
df_compare = pd.read_csv('route20_stop_time_merged.csv')
print(df_compare.shape[0])