# coding: utf-8
from sklearn.datasets import load_boston
from sklearn.feature_selection import VarianceThreshold, chi2, SelectKBest, RFE
import pandas as pd
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['value'] = boston.target
df
df.var(0)
X = boston.data
y = boston.target
from sklearn.linear_model import LinearRegression
p = df['CHAS'].sum() / df.shape[0]
p * (1 - p)
get_ipython().run_line_magic('pinfo', 'VarianceThreshold')
vt = VarianceThreshold(50)
x_lt = vt.fit_transform(X)
x_lt
x_lt.shape
lr = LinearRegression()
lr.fit(x_lt, y)
get_ipython().run_line_magic('pinfo', 'lr.score')
lr.score(x_lt, y)
get_ipython().run_line_magic('pinfo', 'VarianceThreshold')
vt.variances_
x_lv = vt.inverse_transform(X)
X.shape
vt.fit_transform(X)
x_lv = vt.inverse_transform(X)
get_ipython().run_line_magic('pinfo', 'vt.inverse_transform')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('pinfo', 'VarianceThreshold')
vt
vt.get_support
vt.get_support(np.arange(X.shape[1]))
import numpy as np
vt.get_support(np.arange(X.shape[1]))
vt.get_support()
x_lv = X[:, _]
x_lv.shape
get_ipython().run_line_magic('whos', '')
x_lt.shape
X.shape
x_lv = X[:, np.logical_not(vt.get_support())]
x_lv.shape
lr.fit(x_lv, y)
lr.score(x_lv, y)
lr.fit(x_lt, y)
lr.score(x_lt, y)
df.var(0)
low = 70
high = 100
df.var(0) >= low
df.columns[df.var(0) >= low]
df.columns[df.var(0) < low]
xdf = df.drop(df.columns[df.var(0) < low], axis=1)
xdf = xdf.drop(xdf.columns[df.var(0) > high], axis=1)
xdf = xdf.drop(xdf.columns[xdf.var(0) > high], axis=1)
xdf
xdf.shape
xdf['RAD'].value_counts()
lr.fit(xdf[['CRIM', 'RAD']], xdf['value'])
lr.score(xdf[['CRIM', 'RAD']], xdf['value'])
xdf
xdf.var(0)
df.var(0)
df[df.columns[df.var(0) < 0]]
df[df.columns[df.var(0) < 1]]
xdf = _
lr.fit(xdf, y)
lr.score(xdf, y)
df.shape
df
SelectKBest(chi2, k=5).fit_transform(X, y)
from sklearn.feature_selection import f_regression, mutual_info_regression
SelectKBest(f_regression, k=5).fit_transform(X, y)
_.shape
df.head()
xx = SelectKBest(f_regression, k=5).fit_transform(X, y)
lr.fit(xx, y)
lr.score(xx, y)
xx = SelectKBest(mutual_info_regression, k=5).fit_transform(X, y)
lr.score(xx, y)
lr.fit(xx, y)
lr.score(xx, y)
xx = SelectKBest(f_regression, k=10).fit_transform(X, y)
lr.fit(xx, y)
lr.score(xx, y)
f_regression(X, y)
