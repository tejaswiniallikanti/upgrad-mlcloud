# coding: utf-8
import numpy as np
import pandas as pd

df = pd.read_table('data/wiki/training.tsv', parse_dates=['timestamp'])

df['train'] = True
df.loc[df.index[df['timestamp'] >= '2010-02-01'], 'train'] = False

both_arts = np.intersect1d(
    df[df['train']]['article_id'].unique(),
    df[~df['train']]['article_id'].unique())

xdf = df[df['article_id'].isin(both_arts)]
revisions = pd.read_table('data/wiki/comments.tsv', index_col='revision_id')

revisions['length'] = revisions['comment'].str.len()
xdf['revision_length'] = revisions['length']
xdf['revision_length'].fillna(value=0, inplace=True)

ns = pd.read_table('data/wiki/namespaces.tsv', index_col='namespace_id', squeeze=True).to_dict()
xdf['ns'] = xdf['namespace'].apply(lambda x: ns[x])
xdf['namespace'] = xdf.pop('ns')
