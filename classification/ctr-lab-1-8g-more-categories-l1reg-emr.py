#!/usr/bin/env python
# coding: utf-8

# In[1]:


spark


# In[2]:


df = sqlContext.read.csv('s3a://sparkdemonstration/10M.csv', header=True, inferSchema=True)


# In[3]:


catCols = ['C1'] + [f'C{k}' for k in range(14, 22)]
catCols += ['banner_pos', 'site_category', 'device_type', 'device_conn_type',
            'site_id', 'site_domain', 'app_id', 'app_domain', 'app_category', 'device_model']


# In[4]:


from pyspark.sql.functions import udf


# In[5]:


posMapper = udf(lambda x: 0 if x < 0 else x)
df = df.withColumn('C20_1', posMapper(df['C20']))


# In[6]:


catCols.remove('C20')
catCols.append('C20_1')


# In[7]:


from pyspark.ml.feature import OneHotEncoderEstimator


# In[8]:


from pyspark.ml.feature import StringIndexer
for c in ['site_category', 'site_id', 'site_domain', 'app_id', 'app_domain', 'app_category', 'device_model']:
    si = StringIndexer(inputCol=c, outputCol=f'{c}_ix')
    df = si.fit(df).transform(df)
    catCols.remove(c)
    catCols.append(f'{c}_ix')


# In[9]:


from pyspark.sql.types import IntegerType
df = df.withColumn("C20_1int", df['C20_1'].cast(IntegerType()))
catCols.remove('C20_1')
catCols.append('C20_1int')


# In[10]:


encoder = OneHotEncoderEstimator(inputCols=catCols, outputCols=[c + 'Enc' for c in catCols])
enc_model = encoder.fit(df)
encoded = enc_model.transform(df)


# In[11]:


trainCols = [c for c in encoded.columns if c.endswith('Enc')] + ['day', 'hour', 'dayofweek']


# In[12]:


encoded = encoded.withColumn('label', encoded['click'].cast(IntegerType()))


# In[13]:


from pyspark.ml.classification import LogisticRegression


# In[14]:


from pyspark.ml.feature import VectorAssembler


# In[15]:


va = VectorAssembler(inputCols=trainCols, outputCol='features')
encoded = va.transform(encoded)


# In[16]:


auc = []
recall = []
L1 = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5]
for l in L1:
    lr = LogisticRegression(featuresCol='features', labelCol='label', elasticNetParam=1, regParam=l)
    model = lr.fit(encoded)
    result = model.evaluate(encoded)
    auc.append(result.areaUnderROC)
    r = result.recallByLabel
    recall.append(r)
    print(l, r)


# In[17]:


spark.sparkContext.getConf().get('spark.driver.memory')


# In[21]:


auc


# In[22]:


recall


# In[29]:


auc = []
recall = []
L1 = [0.0001, 0.0002, 0.0005, 0.0007, 0.001]
for l in tqdm(L1):
    lr = LogisticRegression(featuresCol='features', labelCol='label', elasticNetParam=1, regParam=l)
    model = lr.fit(encoded)
    result = model.evaluate(encoded)
    auc.append(result.areaUnderROC)
    recall.append(result.recallByLabel)


# In[18]:


auc


# In[19]:


recall


# In[17]:


auc = []
recall = []
L1 = [0.00001, 0.00002, 0.00005, 0.0001, 0.0002]
for l in tqdm(L1):
    lr = LogisticRegression(featuresCol='features', labelCol='label', elasticNetParam=1, regParam=l)
    model = lr.fit(encoded)
    result = model.evaluate(encoded)
    auc.append(result.areaUnderROC)
    recall.append(result.recallByLabel)


# In[20]:


result.precisionByLabel


# In[21]:


auc


# In[22]:


recall


# In[28]:


auc = []
recall = []
L1 = [0.000001, 0.000002, 0.000005, 0.00001]
for l in tqdm(L1):
    lr = LogisticRegression(featuresCol='features', labelCol='label', elasticNetParam=1, regParam=l)
    model = lr.fit(encoded)
    result = model.evaluate(encoded)
    auc.append(result.areaUnderROC)
    recall.append(result.recallByLabel)


# In[29]:


auc


# In[30]:


recall


# In[33]:


auc = []
recall = []
L1 = [0.0000001, 0.0000002, 0.0000005, 0.000001]
for l in tqdm(L1):
    lr = LogisticRegression(featuresCol='features', labelCol='label', elasticNetParam=1, regParam=l)
    model = lr.fit(encoded)
    result = model.evaluate(encoded)
    auc.append(result.areaUnderROC)
    recall.append(result.recallByLabel)


# In[34]:


auc


# In[35]:


recall


# In[ ]:




