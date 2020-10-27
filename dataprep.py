# coding: utf-8
get_ipython().run_line_magic('run', '-i preprocessing.py')
titles = pd.read_table('data/wiki/titles.tsv')
titles.head()
titles.index.name = 'article_id'
titles.columns = ['category', 'timestamp', 'namespace', 'redirect', 'title', 'related_page', 'last']
titles.head()
del titles['last']
title.to_csv('data/wiki/titles-rev.tsv', sep='\t')
titles.to_csv('data/wiki/titles-rev.tsv', sep='\t')
titles.head()
ns
titles['namespace'] = titles['namespace'].apply(lambda x: ns[x])
titles.head()
xdf.shape
titles.shape
articles = xdf['article_id'].unique()
articles.shape
titles = titles.loc[articles]
artiles[:5]
articles[:5]
articles[-5:]
pd.isnull(articles).sum()
titles.head()
pd.isnull(titles.index).sum()
xx = titles.loc[articles]
np.intersect1d(articles, titles.index).shape
artciles.shape
articles.shape
531970 - 525958
articles = np.intersect1d(articles, titles.index)
titles = titles.loc[articles]
xdf = xdf[xdf['article_id'].isin(articles)]
titles.head()
titles['start'] = pd.NaT
titles['end'] = pd.NaT
start = xdf.groupby('article_id').min()['timestamp']
start = xdf.groupby('article_id')['timestamp'].min()
start.shape
titles.shape
titles['start'] = start
end = xdf.groupby('article_id')['timestamp'].max()
titles['end'] = end
titles['lifetime'] = titles['end'] = titles['start']
titles['lifetime'].describe()
titles['lifetime'].head()
titles['end'].head()
titles['start'].head()
titles[] - titles['start']
titles['end'] - titles['start']
titles.head()
del titles['lifetime']
titles['lifetime'] = titles['end'] - titles['start']
titles.head()
xx = df['lifetime']
xx = titles['lifetime']
xx.dt.days.head()
xx.dt.days.describe()
xx.head()
xx.tail()
titles.head()
(df['start'] == df['end']).all()
(titles['start'] == titles['end']).all()
xdf['timestamp'].head()
xdf.head()
starts = xdf.groupby('article_id')['timestamp'].min()
xdf[xdf['article_id'] == 9445560]['timestamp']
xdf[xdf['article_id'] == 9445560]['timestamp'].min()
starts.head()
starts[9445560]
titles['start'] = xdf.groupby('article_id')['timestamp'].min()
titles['end'] = xdf.groupby('article_id')['timestamp'].max()
(titles['start'] == titles['end']).all()
titles['lifetime'] = titles['start'] - titles['end']
titles.head()
titles['lifetime'] = (titles['end'] - titles['start']).dt.days
titles.head()
titles['lifetime'].describe()
get_ipython().run_line_magic('matplotlib', '')
titles['lifetime'].hist(bins=100)
del titles['start']
del titles['end']
titles.head()
categories = pd.read_table('data/wiki/categories.tsv', index_col='category_id', squeeze=True).to_dict()
categories
titles['category'] = titles['category'].apply(lambda x: categories[x])
titles.head()
xdf.head()
xdf['reverted'].value_counts()
titles['p_revert'] = xdf.groupby('article_id')['reverted'].mean()
titles.head()
xdf[xdf['article_id'] == 12]
xx = _
xx['reverted'].sum() / xx.shape[0]
gb = xdf.groupby('article_id')
titles['M_delta'] = gb['delta'].mean()
titles['S_delta'] = gb['delta'].std()
titles['M_size'] = gb['cur_size'].mean()
titles['S_size'] = gb['cur_size'].std()
xdf['revision_length'].describe()
xdf['revision_length'].hist(bins=100)
xdf['revision_length'].hist(bins=10)
revisions.head()
titles['M_comments'] = gb['revision_length'].mean()
titles['S_comments'] = gb['revision_length'].std()
titles.head()
titles['title'].value_counts().head()
titles[titles['title'] == 'Anarchism']
titles['category'].head()
titles['category'].value_counts()
titles['redirect'].value_counts()
titles.head()
titles.tail()
titles[titles['related_page'] > 0].head()
titles['related_page'] = titles['related_page'] > 0
titles.head()
titles['n_count'] = 0
xx = gb.count()
xx.shape
xx.head()
xdf.loc[12].shape
xdf.loc[12].head()
xdf[xdf['article_id'] == 12].shape
titles['n_count'] = gb['user_id'].count()
titles.head()
titles['n_count'].hist()
titles['n_count'].apply(np.log).hist()
titles['n_count'].apply(np.log).hist(bins=100)
titles['n_count'].apply(np.log10).hist(bins=100)
titles.head()
titles.shape
titles.to_csv('data/wiki/articles.tsv')
