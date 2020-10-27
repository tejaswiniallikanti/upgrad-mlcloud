# coding: utf-8
import numpy as np

DTYPES = {
    'banner_pos': np.int8,
    'device_type': np.int8,
    'device_conn_type': np.int8,
    'month': np.int8,
    'day': np.int8,
    'dayofweek': np.int8,
    'hour': np.int16,
    'C1': np.int32,
    'C14': np.int32,
    'C15': np.int32,
    'C16': np.int32,
    'C17': np.int32,
    'C18': np.int16,
    'C19': np.int32,
    'C21': np.int16,
}

df = pd.read_csv('data/avazu/10M.csv', dtype=DTYPES)

vcs = df['C14'].value_counts()
c14_keep = vcs[vcs > 1].index
df = df[df['C14'].isin(c14_keep)]

vcs = df.groupby('site_category')['click'].mean()
sc_keep = vcs[vcs > 0].index
df = df[df['site_category'].isin(sc_keep)]

df = df[df['device_type'] != 2]
vcs = df['site_id'].value_counts()
sid1 = vcs[vcs == 1].index

appcat_gb = df.groupby('app_category')['click'].mean()
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
        
