# df3 = pd.read_csv('bus_avl_2019-09-03.csv')
# df4 = pd.read_csv('bus_avl_2019-09-04.csv')
# df5 = pd.read_csv('bus_avl_2019-09-05.csv')
# df6 = pd.read_csv('bus_avl_2019-09-06.csv')
#
# df_main = pd.DataFrame()
#
# base_date = '2019-09-03 00:00:00'
# for df in (df3, df4, df5, df6):
#     d = df[df['route_id'] == str(20)]
#     d = d[['route_id', 'trip_id', 'stop_sequence', 'event_time', 'departure_time',
#            'dwell_time', 'passenger_load']]
#     d['base_date'] = [base_date] * len(d.index)
#     d['avl_sec'] = d['departure_time'].astype('datetime64[ns]') - d['base_date'].astype('datetime64[ns]')
#     d['avl_sec'] = d['avl_sec'].dt.total_seconds()
#     d = d.dropna(subset=['avl_sec'])
#     d['avl_sec'] = d['avl_sec'].round(decimals=1)
#     d = d.drop('base_date', axis=1)
#     df_main = df_main.append(d, ignore_index=True)

# df_main['trip_id'] = df_main['trip_id'].replace('', np.nan)
# df_main = df_main.dropna(subset=['trip_id'])
# df_main['trip_id'] = df_main['trip_id'].astype(str).str[:-2]
# df_main['trip_id'] = df_main['trip_id'].astype(int)
# df_main['route_id'] = df_main['route_id'].astype(int)
# df_main.to_csv('route20_stop_time_dwell.csv', index=False)