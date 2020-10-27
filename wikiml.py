# coding: utf-8
import pandas as pd
from sklearn.linear_model import LogisticRegressionCV
df = pd.read_csv('data/wiki/articles.tsv', index_col='article_id')
df.head()
get_ipython().run_line_magic('pinfo', 'pd.get_dummies')
catCols = ['category', 'namespace']
catData = []
for c in catCols:
    catData.append(pd.get_dummies(df[c], prefix=c, drop_first=True))
    
catData = pd.DataFrame(catData, axis=1)
catData = pd.concat(catData, axis=1)
catData.head()
df.head()
df['related_page'] = df['related_page'].astype(int)
numCols = ['redirect', 'related_page', 'lifetime', 'p_revert', 'M_delta', 'S_delta', 'M_size', 'S_size', 'M_comments', 'S_comments', 'n_count']
XDF = pd.concat([df[numCols], catData], axis=1)
XDF.head()
ix = XDF.index.values.copy()
import numpy as np
np.random.shuffle(ix)
X = XDF.loc[ix]
y = X.pop('n_count')
y.head()
XDF.head()
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(XDF.values, y)
lr.score(XDF.values, y)
from sklearn import linear_model as lm
r = lm.Ridge().fit(XDF.values, y)
get_ipython().run_line_magic('pinfo', 'r.score')
r.score(XDF.values, y)
r = lm.Ridge(alpha=0.5).fit(XDF.values, y)
r.score(XDF.values, y)
get_ipython().run_line_magic('pinfo', 'lm.RidgeCV')
get_ipython().run_line_magic('pinfo', 'lm.RidgeCV')
rcv = lm.RidgeCV(alphas=[0.001, 0.01, 0.1, 1, 10, 100, 1000], cv=5)
rcv.fit(XDF.values, y)
rcv
rcv.score(XDF.values, y)
get_ipython().set_next_input('lasso = lm.LassoCV');get_ipython().run_line_magic('pinfo', 'lm.LassoCV')
lasso = lm.LassoCV(n_jobs=-1, cv=5)
lasso.fit(XDF.values, y)
lasso.score(XDF.values, y)
lasso.coef_
rcv.coef_
ecv = lm.ElasticNetCV()
ecv.fit(XDF.values, y)
ecv.score(XDF.values, y)
from sklearn.feature_selection import RFECV
RFECV.head()
RFECV
lr = lm.LinearRegression()
rfecv = RFECV()
rfecv = RFECV(lr, cv=5, n_jobs=-1)
rfecv.fit(XDF.values, y)
rfecv.grid_scores_
rfecv.grid_scores_.max()
XDF.var(0)
get_ipython().run_line_magic('whos', '')
df.head()
X.shape
X.head()
X.columns
XDF.columns
XDF.groupby('redirect')['n_count'].mean()
get_ipython().run_line_magic('matplotlib', '')
import seaborn as sns
X.var(0)
XDF.groupby('related_page')['n_count'].mean()
XX = X[[c for c in X if not c.startswith('M_')]]
XX = XX[[c for c in XX if not c.startswith('S_')]]
XX.columns
XX.var(0).plot(kind='bar')
XX.drop(['lifetime'], axis=1).var(0).plot(kind='bar')
rfecv.fit(XX, y)
rfecv.grid_scores_.max()
rfecv.score(XX, y)
lasso
lasso.fit(XX, y)
lasso.score(XX, y)
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
XX.head()
get_ipython().run_line_magic('pinfo', 'SelectKBest')
XX.shape
for i in range(2, 20):
    best = SelectKBest(f_regression, k=i)
    XXX = best.fit_transform(XX.values)
    lr = lm.LinearRegression().fit(XXX, y.values)
    print(i, lr.score(XXX, y.values))
    
for i in range(2, 20):
    best = SelectKBest(f_regression, k=i)
    XXX = best.fit_transform(XX.values, y.values)
    lr = lm.LinearRegression().fit(XXX, y.values)
    print(i, lr.score(XXX, y.values))
    
ecv = lm.ElasticNetCV(l1_ratio=[0.1, 0.2, 0.5, 0.75, 0.8, 0.89, 0.9, 0.95, 0.99, 1])
ecv.fit(XX.values, y.values)
ecv.score(XX, y)
XDF.columns
for c in XDF:
    if c.startswith('M_') or c.startswith('S_'):
        print(c, XDF[c].var())
        
XDF['n_count'].var()
XX.var(0)
XXX = XDF[[c for c in XDF if c.startswith('M_')]]
XXX = XXX[[c for c in XXX if c.startswith('S_')]]
XXX.head()
XXX = XDF[[c for c in XDF if c.startswith('M_') or c.startswith('S_')]]
XXX.head()
XXX['lifetime'] = XDF['lifetime']
XXX.head()
y.shapoe
y.shape
XXX.shape
ecv.fit(XXX.values, y.values, n_jobs=-1)
ecv.n_jobs = -1
ecv.fit(XXX.values, y.values, n_jobs=-1)
ecv.fit(XXX.values, y.values)
ecv.score(XXX.values, y.values)
