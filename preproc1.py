# coding: utf-8
import pandas as pd
import numpy as np

df = pd.read_csv('train.csv', parse_dates=['key'])
del df['pickup_datetime']

df = df[df['fare_amount'] <= 250]
df = df[df['passenger_count'] <= 10]
df = df[df['passenger_count'] > 0]

LEFT, RIGHT, BOTTOM, TOP = -75, -73, 40, 42
df = df[df['pickup_longitude'] >= LEFT]
df = df[df['pickup_longitude'] <= RIGHT]
df = df[df['pickup_latitude'] <= TOP]
df = df[df['pickup_latitude'] >= BOTTOM]
df = df[df['dropoff_latitude'] >= BOTTOM]
df = df[df['dropoff_latitude'] <= TOP]
df = df[df['dropoff_longitude'] <= RIGHT]
df = df[df['dropoff_longitude'] >= LEFT]

x1 = df['pickup_longitude']
y1 = df['pickup_latitude']
x2 = df['dropoff_longitude']
y2 = df['dropoff_latitude']
df['l1'] = np.abs(x1 - x2) + np.abs(y1 - y2)

df['key'] = df['key'].dt.tz_localize('UTC')
df['key'] = df['key'].dt.tz_convert('EST')
for k in 'year month dayofweek hour'.split():
    df[k] = getattr(df['key'].dt, k)
