#!/usr/bin/env python
# coding: utf-8


# In[2]:


import streamlit as st
import pandas as pd
import numpy as np


# In[3]:


HairEye = pd.read_csv("HairEyeColor.csv")


# In[4]:


st.title("Hair Eye Colour Database")


# In[6]:


InputHair = st.sidebar.selectbox("Select Hair Colour", ("Brown", "Black", "Blond", "Red"))


# In[ ]:


HairEyeSelect = HairEye[HairEye["Hair"] == InputHair]


# In[ ]:


st.dataframe(HairEyeSelect)

