# df1 = pd.read_csv('in/raw/bus_avl_2019-09-10.csv')
# df2 = pd.read_csv('in/raw/bus_avl_2019-09-11.csv')
# df3 = pd.read_csv('in/raw/bus_avl_2019-09-12.csv')
# df4 = pd.read_csv('in/raw/bus_avl_2019-09-13.csv')
# date1 = '2019-09-10 00:00:00'
# date2 = '2019-09-11 00:00:00'
# date3 = '2019-09-12 00:00:00'
# date4 = '2019-09-13 00:00:00'
# df_sched = pd.read_csv('in/raw/route20_stop_time.csv')
# df_sched = df_sched[['trip_id', 'stop_sequence', 'schd_sec', 'stop_id']]
# df_main = pd.DataFrame()
#
# for joint in ((df1, date1), (df2, date2), (df3,date3), (df4, date4)):
#     df, bdate = joint
#     d = df[df['route_id'] == str(20)]
#     d = d[['route_id', 'trip_id', 'stop_sequence', 'event_time', 'departure_time']]
#     d['trip_id'] = d['trip_id'].replace('', np.nan)
#     d = d.dropna(subset=['trip_id'])
#     d = d.astype({'trip_id': 'int64'})
#     d = d.rename(columns={'event_time': 'avl_arr_time', 'departure_time': 'avl_dep_time'})
#
#     d['base_date'] = [bdate] * len(d.index)
#
#     d['avl_arr_sec'] = d['avl_arr_time'].astype('datetime64[ns]') - d['base_date'].astype('datetime64[ns]')
#     d['avl_arr_sec'] = d['avl_arr_sec'].dt.total_seconds()
#     d['avl_arr_sec'] = d['avl_arr_sec'].round(decimals=1)
#
#     d['avl_dep_sec'] = d['avl_dep_time'].astype('datetime64[ns]') - d['base_date'].astype('datetime64[ns]')
#     d['avl_dep_sec'] = d['avl_dep_sec'].dt.total_seconds()
#     d['avl_dep_sec'] = d['avl_dep_sec'].round(decimals=1)
#
#     d = d.drop('base_date', axis=1)
#
#     d = d.merge(df_sched, left_on=['trip_id', 'stop_sequence'], right_on=['trip_id', 'stop_sequence'])
#     df_main = df_main.append(d, ignore_index=True)
# df_main = df_main.sort_values(by=['trip_id', 'stop_sequence'])
# df_main = df_main.drop_duplicates(subset=['avl_dep_time'])
# df_main['avl_dep_time'] = df_main['avl_dep_time'].replace('', np.nan)
# df_main = df_main.dropna(subset=['avl_dep_time'])
# df_main.to_csv('in/raw/rt20_extra.csv', index=False)