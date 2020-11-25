#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def CountMutations (x,y):
    S=0
    for i in range(len(x)):
        if x[i] != y[i]:
            S=S+1
    print (S)


# In[1]:


CountMutations ("AAAA","AAAT")
CountMutations ("AAAA","CCCT")
CountMutations ("AAAA","AAAA")

