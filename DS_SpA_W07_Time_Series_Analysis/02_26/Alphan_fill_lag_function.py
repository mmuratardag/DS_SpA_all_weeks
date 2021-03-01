def fill_lags(df_lag,df_filler,N,lag_prefix='lag',col_remainder='remainder',t_unit='days'):
    '''
    Fill the lags for a test_df or a future_df used in a timeseries analysis
    df_lag: DataFrame (Future) with the lags to be filled
    df_filler: DataFrame (Past) with the remainders to be used as lags
    N: Number of lags
    lag_prefix: The prefix of the lag columns as a string, it is assumed that the lag columns are named as lag1, lag2,...,lagN\n
    where (lag) is the prefix
    col_remainder: The name of the remainder column in the DataFrame (Past)
    t_unit: TimeDelta unit for the minimum timestep in the index, takes TimeDelta keyword values e.g., days, months, years etc.
    '''
    #Get last N rows of the remainders from the filler dataframe
    df_temp = df_filler[[f'{col_remainder}']][-N:].copy()
    #Time (days) forward as much as the lags
    df_temp.index += pd.Timedelta(**{f'{t_unit}':N})
    #For lag i shift remainders by i-N+1 e.g., for lag1, N=3 shift remainder by 2 for lag2, N=3, shift remainder by 1 etc. and add to df   
    for i in range(N):
        df_temp[f'{lag_prefix}{i+1}'] = df_temp[f'{col_remainder}'].shift(i-N+1)
    #Fill the lags with the created DataFrame
    return df_lag.fillna(df_temp)