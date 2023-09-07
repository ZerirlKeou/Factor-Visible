def Rank(df):
    rank = df.rank(ascending=False,method='dense')
    rank_percent = rank/rank.max()*100
    return rank_percent
