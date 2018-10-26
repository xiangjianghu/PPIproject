import numpy as np
import pandas as pd
#行业收益计算
ind=pd.read_excel(r'C:\Users\xiangjiang.hu\Desktop\sw1.xlsx',index_col=[0])
pct=pd.read_csv(r'C:\Users\xiangjiang.hu\Desktop\data2\pct_prm.csv',index_col=[0])
temp=pd.concat([ind,pct.T],axis=1,join='inner')
temp
#这里由于股票编码发生了变化，所以需要重新标准化
temp1=temp.iloc[:,2:]
x1=temp1.mean()
temp2=temp1.apply(lambda x:x-x1,axis=1)
temp2
temp3=pd.concat([ind,temp2],axis=1,join='inner')
x=np.array(temp3.columns[2:])
gain=temp3[x].groupby(temp3[u'申万一级行业']).mean()
gain.to_excel(r'C:\Users\xiangjiang.hu\Desktop\10project5\pct_ind.xlsx')


#PPI回测
pct=pd.read_excel(r'C:\Users\xiangjiang.hu\Desktop\10Project5\pct_ind.xlsx',index_col=[0]).T
PPI=pd.read_excel(r'C:\Users\xiangjiang.hu\Desktop\10Project5\PPI14-18.xlsx',index_col=[0])
del PPI[20180809]
pct1=pct.loc[20140109:]
x=np.array(PPI.columns[1:])
gain=(PPI[x].groupby(PPI[u'申万一级行业']).mean()-100).T
gain1=gain.loc[pct1.index,:]
gain1.fillna(method='pad',inplace=True)
gain1=gain1.loc[:20180716]
gain1
pct2=pct1.loc[20140110:,gain1.columns]
pct2.index=gain1.index
pct2
import datetime
M=pct2.index
M=pd.Series(M)
for i in range(len(M)):
    M[i]=datetime.datetime.strptime(str(pct2.index[i]),'%Y%m%d')
pct2.index=M

plt.figure(figsize=(7.5,5))
plt.plot(pct2.cumsum())
plt.show() 

#cumsum图
factor=gain1.rank(axis=1,pct=True)
A=factor.as_matrix()
B=pct2.as_matrix()
final=np.array([(A.reshape(np.size(A))),(B.reshape(np.size(B)))])
final1=pd.DataFrame(final.T)
final2=final1.sort_values(0)
final3=final2.dropna()
plt.plot(final3[0],final3[1].cumsum())
plt.show() 

#分五组进行计算
temp=pct2.mean(axis=1)
pct3=pct2.apply(lambda x:(x-temp),axis=0)
P1=((factor<=0.2)*pct3).mean(axis=1)+1
P2=(((factor>0.2)&(factor<=0.4))*pct3).mean(axis=1)+1
P3=(((factor>0.4)&(factor<=0.6))*pct3).mean(axis=1)+1
P4=(((factor>0.6)&(factor<=0.8))*pct3).mean(axis=1)+1
P5=((factor>0.8)*pct3).mean(axis=1)+1
P6=(P1-P5)/2+1

import datetime
M=P1.index
M=pd.Series(M)
for i in range(len(P1)):
    M[i]=datetime.datetime.strptime(str(P1.index[i]),'%Y%m%d')
P1.index=M
P2.index=M
P3.index=M
P4.index=M
P5.index=M
P6.index=M
plt.figure(figsize=(15,10))
plt.plot(P1.cumprod()-1,label='1')
plt.plot(P2.cumprod()-1,label='2')
plt.plot(P3.cumprod()-1,label='3')
plt.plot(P4.cumprod()-1,label='4')
plt.plot(P5.cumprod()-1,label='5')
plt.plot(P6.cumprod()-1,label='LS')
plt.legend()
plt.show()
#Fama—French三因子检测
factor_3=pd.read_csv(r'C:\Users\xiangjiang.hu\Desktop\project2\factor_3.csv',index_col=[0])
temp11=pd.read_csv(r'C:\Users\xiangjiang.hu\Desktop\project1\mkt_cap_ard.csv',index_col=[0])
factor_3.index=temp11.index
factor3=factor_3.loc[20140109:,'1':]
factor3
pct4=pct3.loc[factor3.index,:]
Factor=factor.loc[factor3.index,:]
Factor
p5=(((factor>0.8))*pct4).mean(axis=1)
p6=(p5-p1)/2
L6=pd.concat([p6,factor3],axis=1,join='inner')
L6.to_excel(r'C:\Users\xiangjiang.hu\Desktop\10Project5\L6regression.xlsx')
