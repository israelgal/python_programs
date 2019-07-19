#!/usr/bin/env python
# coding: utf-8

# In[3]:


def ack(m,n):
     """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m==0:
        n=n+1
        return n
    if m>0 and n==0:
        value_ack = ack(m-1,1)
        return value_ack
    if m>0 and n>0:
        value_ack = ack(m-1,ack(m,n-1))
        return value_ack
        
ack(0,2)        


# In[5]:


def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))


print(ackermann(0, 2))


# In[ ]:




