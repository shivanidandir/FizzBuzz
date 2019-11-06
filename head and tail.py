
# coding: utf-8

# In[11]:


import numpy as np
np.random.seed(123)


# In[12]:


coin=np.random.randint(0,2)
print(coin)
if coin==0:
    print("heads")
else:
    print("tails")

