import tushare as ts
import numpy as np
import factor
import WriteCSV
import pandas as pd
import generate_evoluation

alpha1 = []
pct_chg = []
alpha2=[]
rvi=[]

if __name__ == '__main__':
    ts.set_token("9719560105905c9ea068aec2f4834ad3932cb6e4778b24ef0f8acc2f")
    pro = ts.pro_api()
    pool = ['000001.SZ', '000002.SZ', '000004.SZ', '000005.SZ', '000008.SZ', '000004.SZ', '600010.SH', '600020.SH']
    for i in pool:
        df = pro.daily(ts_code=i, start_date='20170602', end_date='20230421')
        dfy = pro.daily(ts_code=i, start_date='20170601', end_date='20230420')
        # print(df)
        # macd, dea, dif = factor.Macd(df)
        # cci = factor.Cci(df, 14)
        # rsi = factor.relative_strength_index(df)
        # liangbi = factor.liangbi(df)
        # alpha1.append(factor.alpha1(df).tolist())
        # alpha2.append(factor.alpha2(df).tolist())
        pct_chg.append(dfy['pct_chg'].tolist())
        rvi.append(factor.calculate_RVI(df).tolist())
        if (i == 0):
            type = 'w'
        else:
            type = 'a'
        # WriteCSV.writeXY(name='macd.csv', X=macd.tolist(), y=df['pct_chg'].tolist(), type=type)
        # WriteCSV.writeXY(name='cci.csv', X=cci.tolist(), y=df['pct_chg'].tolist(), type=type)
    # print(rvi)
    # # print(pct_chg)
    # print(len(rvi))
    for i in range(len(rvi)):
        name = 'rvi_' + str(i) + '.csv'
        # print(name)
        print(rvi[i])
        WriteCSV.writeMultiRow(name=name, X=rvi[i], y=pct_chg[i], type='w')
    # print(len(alpha1[0]))
    # print(len(pct_chg[0]))
    # score = generate_evoluation.fitness(alpha1[0], pct_chg[0])
    # print(score)
    # WriteCSV.writeXY(name='liangbi.csv', X=liangbi.tolist(), y=df['pct_chg'].tolist(), type=type)
    # WriteCSV.writeXY(name='rsi.csv', X=rsi.tolist(), y=df['pct_chg'].tolist(), type=type)
