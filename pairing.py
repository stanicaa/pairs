import pandas as pd
import datetime
from pandas.tseries.offsets import BDay

#building the relevant functions

#reading the excel file t
def proc(t):
    fi=pd.read_excel(t, index_col=0) #skiprows=n allows you to start at row n
    g=fi.drop(fi.index[0])
    return g

#calculating and identifying all the pairs
def pairing(ll, bb):
    c=list(bb)
    pairs=[]
    for i in c:
        cc=c.copy()
        cc.remove(i)
        for k in cc:
            a=bb[i]-bb[k]
            max=a.max()
            min=a.min()
            limit=(max-min)/ll
            aa=len(a)
            value=a.iloc[aa-1]
            if (value-min)<limit or (max-value)<limit:
                #print('Found PAIR: ',i,' ',k)
                if (i,k) not in pairs and (k,i) not in pairs:
                    pairs.append((i,k))
    return pairs

#searching for a specific stock pair
def search(p):
    stock=input('Stock please: ')
    s=stock+' JT Equity'
    for i in p:
        if s in i:
            print(i)

#getting the correlations for a specific stock
def corrs(d):
    stock=input('Stock please: ')
    s=stock+' JT Equity'
    ss=d[s]
    ss=ss.sort_values()
    print('TOP CORRELATIONS: ', ss.tail(20))
    print('--------------------------------')
    print('BOTTOM CORRELATIONS: ', ss.head(20))
    return

#keeping only the weekdays
def bsd(a):
    isBusinessDay = BDay().onOffset
    match_series = pd.to_datetime(a.index).map(isBusinessDay) #bC is the DataFrame we work on
    a=a[match_series]
    return a

#the function putting it all together
def pairs(t):
    bb=proc(t)
    bb=bb.astype(float)
    bb=bsd(bb)
    p=pairing(20, bb)
    search(p)
    d=bb.corr()
    corrs(d)



