import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
SWindex=pd.read_excel(r'C:\Users\xiangjiang.hu\Desktop\10Project5\SWIndustryClose.xlsx',index_col=[0])
swpct=((SWindex-SWindex.shift(1))/SWindex.shift(1)).loc[20140109:]
swpct_M60=((SWindex-SWindex.shift(1))/SWindex.shift(1)).loc[20131017:].rolling(60).mean().dropna()
test=swpct.rank(axis=1)
group1=test[test>=22]
group2=(test[(test<22) & (test>=15)])
group3=(test[(test<15) & (test>=8)])
group4=test[test<=7]
test1=swpct_M60.rank(axis=1)
Group1=test1[test1>=22]
Group2=(test1[(test1<22) & (test1>=15)])
Group3=(test1[(test1<15) & (test1>=8)])
Group4=test1[test1<=7]
Group4.loc[20140110:].count().sum()
temp=Group4.shift()
y1=(temp-group1).count(axis=0).sum()
y2=(temp-group2).count(axis=0).sum()
y3=(temp-group3).count(axis=0).sum()
y4=(temp-group4).count(axis=0).sum()
(np.array([y1,y2,y3,y4])/7714.0*100).sum()
(np.array([y1,y2,y3,y4])/7714.0*100)
