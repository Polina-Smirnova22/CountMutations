#!/usr/bin/env python
# coding: utf-8

# In[3]:


def CountSize (x, y):
    counter = 0
    if len(x) == len (y):
        for i in range (len(x)):
            if x[i] != y[i]:
                counter += 1
        print (counter)
    else: print ("Wrong size")


# In[1]:


CountSize("AAAA" , "AAAT")
CountSize("AAAA" , "CCCT")
CountSize("AAAA" , "AAAA")


# In[ ]:




