import pandas as pd

base_date = '2019-09-03 00:00:00'
df_final = pd.read_csv('route20_stop_time_final.csv')
df_no_dwell = pd.read_csv('route20_stop_time.csv')
df_final['base_date'] = [base_date] * len(df_final.index)
time_tuples = (('event_time', 'avl_sec'), ('departure_time', 'avl_dep_sec'))
for t in time_tuples:
    df_final[t[1]] = df_final[t[0]].astype('datetime64[ns]') - df_final['base_date'].astype('datetime64[ns]')
    df_final[t[1]] = df_final[t[1]].dt.total_seconds()
    df_final = df_final.dropna(subset=[t[1]])
    df_final[t[1]] = df_final[t[1]].round(decimals=1)
df_final = df_final.drop('base_date', axis=1)
cols = df_no_dwell.columns.tolist()
cols += ['dwell_time', 'passenger_load', 'departure_time', 'avl_dep_sec']
cols.remove('diff')
df_final = df_final[cols]
df_final.to_csv('route20_stop_time_merged.csv', index=False)

