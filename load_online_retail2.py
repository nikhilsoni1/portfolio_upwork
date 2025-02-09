#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from db.database import SessionLocal, init_db
from db.repositories import OnlineRetail2Repository
import numpy as np
from tqdm import tqdm


# In[2]:


df = pd.read_csv("/Users/nikhilsoni/Downloads/online_retail_II.csv")


# In[3]:


mapping_dict = {
    "id": "id",
    "Invoice": "invoice_no",
    "StockCode": "stock_code",
    "Description": "description",
    "Quantity": "quantity",
    "InvoiceDate": "invoice_date",
    "Price": "unit_price",
    "Customer ID": "customer_id",
    "Country": "country",
}
df1 = df.copy()
df1 = df1.reset_index(names="id")
df1 = df1.rename(columns=mapping_dict)
records = df1.to_dict(orient="records")


# In[5]:


db_session = SessionLocal()
repository = OnlineRetail2Repository(db_session)
repository.bulk_create(records)

