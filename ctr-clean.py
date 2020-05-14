# coding: utf-8
import pandas as pd
get_ipython().run_line_magic('run', '-i avazu-types.py')
df = pd.read_csv('data/avazu/10M.csv', dtype=DTYPES)
df['C1'].value_counts()
df.groupby('C1').agg('click').mean()
df.dtypes
df.groupby('banner_pos').agg('click').mean()
_.sum()
for c in [f'C{k}' for k in range(14, 22)]:
    df[c].value_counts().tail()
    
for c in [f'C{k}' for k in range(14, 22)]:
    print(df[c].value_counts().tail())
    
    
for c in [f'C{k}' for k in range(14, 22)]:
    print(c, df[c].nunique())
    
vcs = df['C14'].value_counts()
vcs.tail()
vcs.tail(20)
vcs.tail(30)
(vcs == 1).sum()
c14_drop = vcs[vcs == 1].index
c14_keep = vcs[vcs > 1].index
df = df[df['C14'].isin(c14_keep)]
df.shape
df.head()
df['site_category'].nunique()
df['site_category'].value_counts()
vcs = _
sc_keep = vcs[vcs > 1].index
sc_drop = vcs[vcs < 10].index
df[df['site_category'].isin(sc_drop)]['click']
df.groupby('site_category')['click'].mean()
vcs = _
sc_keep = vcs[vcs > 0].index
df = df[df['site_category'].isin(sc_keep)]
df['device_type'].nunique()
df.groupby('device_type')['click'].mean()
df['device_type'].value_counts()
df = df[df['device_type'] != 2]
df.head()
df.shape
df['device_type'].nunique()
df['device_conn_type'].nunique()
df['device_conn_type'].value_counts()
df.groupby('device_conn_type')['click'].mean()
df['site_id'].nunique()
df['site_id'].value_counts()
vcs = _
vcs[vcs == 1]
sid1 = vcs[vcs == 1].index
df[df['site_id'].isin(sid1)]['click'].sum()
sid1.shape
120 / 565
df['site_domain'].nunique()
df['site_domain'].value_counts().tail()
vcs = df['site_domain'].value_counts()
(vcs == 1).sum()
sd1 = vcs[vcs == 1].index
sd1
sd1.shape
df[df['site_domain'].isin(sd1)]['click'].sum() / _[0]
df['app_id'].nunique()
vcs = df['app_id'].value_counts()
vcs.tail()
aid = vcs[vcs == 1].index
df[df['app_id'].isin(aid)]['click'].sum() / aid.shape[0]
df['app_domain'].nunique()
vcs = df['app_domain'].value_counts()
vcs.tail()
adm = vcs[vcs == 1].index
df[df['app_domain'].isin(adm)]['click'].sum() / adm.shape[0]
df['app_category'].nunique()
df['app_category'].value_counts()
df.groupby('app_category')['click'].mean()
appcat_gb = _
appcat_keep = appcat_gb[appcat_gb > 0].index
df = df[df['app_category'].isin(appcat_keep)]
df.shape
9999999 - df.shape[0]
df['device_model'].nunique()
vcs = df['device_model'].value_counts()
vcs.tail()
dm1 = vcs[vcs == 1].index
dm1.shape
df[df['device_model'].isin(dm1)]['click'].sum() / dm1.shape[0]
df.columns
y = df.pop('click')
numCols = ['month', 'dayofweek', 'day', 'hour']
catCols = [c for c in df if c not in numCols]
xCat = pd.get_dummies(df[catCols], sparse=True)
xCat = pd.get_dummies(df[catCols], sparse=True, drop_first=True)
type(xCat)
xCat.shape
xCat.head()
type(xCat.values)
xNum = df[numCols].values
xNum.shape
from scipy.sparse import lil_matrix
xNum = lil_matrix(xNum)
X
from scipy.sparse import hstack
dtype(xCat)
type(xCat)
get_ipython().run_line_magic('clear', '')
xCat = xCat.sparse.to_coo()
xCat.columns
del xCat
import gc
gc.collect()
get_ipython().run_line_magic('whos', '')
catData = []
import tqdm
for c in tqdm(catCols):
    catData.append(pd.get_dummies(df[c], sparse=True, drop_first=True))
    
for c in tqdm.tqdm(catCols):
    catData.append(pd.get_dummies(df[c], sparse=True, drop_first=True))
    
xx = catData[0]
xx
xx.dtpe
xx.dtype
xx.dtypes
xx.sparse
get_ipython().run_line_magic('pinfo', 'hstack')
xCat = hstack([c.sparse.to_coo() for c in catData])
type(catData)
catData[0]
catData[0].sparse.to_coo()
catData[0].sparse.to_csr()
xx
xx.values
_.shape
xx.sparse._parent
xx.sparse._parent.dtypes
from scipy.sparse import lil_matrix
catData = [lil_matrix(x.values) for x in catData]
newCat = []
for c in tqdm.tqdm(catData):
    try:
        newCat.append(c.sparse.to_coo())
    except KeyError:
        newCat.append(lil_matrix(c.values))
        
catCols
df[catCols].dtype
df[catCols].dtypes
for c in catData:
    break
    
c
c.dtypes
newCat = []
gc.collect()
for c in tqdm.tqdm(catData):
    try:
        newCat.append(c.sparse.to_coo())
    except KeyError, IndexError:
        newCat.append(lil_matrix(c.values))
        
for c in tqdm.tqdm(catData):
    try:
        newCat.append(c.sparse.to_coo())
    except (KeyError, IndexError):
        newCat.append(lil_matrix(c.values))
        
