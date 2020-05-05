#!/usr/bin/env python
# coding: utf-8

# ### Starbucks'tan çıkan  insanları yolcu kabul edelim, bir taksicinin de en yakın yolcuyu bulmasını sağlayalım. Taksicinin konumu bir sabit olarak alalım , buradaki yolcuların koordinaatlarını taksiye yapılan istek olarak belirleyelim. Taksiciye de onun konumuna en yakın olan yolcuları gösterelim.

# In[79]:


from math import sin, cos, sqrt, atan2, radians

import pandas as pd


df = pd.read_csv('directory.csv')
driver_cordinates = [{"lat":40.912522,"long":42.874365}]
df=df[df['Country']=='TR'].reset_index()
df = df[df['City']=='Istanbul'].reset_index()
df = df[['Latitude','Longitude']]
mesafe = []
driver_cordinates = [{"lat":41.0429528,"long":28.9970722}]
for i in range (0,len(df)):
    R = 6373.0

    lat1 = radians(driver_cordinates[0]['lat'])
    lon1 = radians(driver_cordinates[0]['long'])
    lat2 = radians(df['Latitude'][i])
    lon2 = radians(df['Longitude'][i])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
        

    distance = R * c
    yakinlik = {"passengerId":i+1,"km between driver and passenger":round(distance,10)} 
    mesafe.append(yakinlik)
df_mesafe = pd.DataFrame(mesafe)
min_distance = df_mesafe['km between driver and passenger'].min()
df_mesafe = df_mesafe[df_mesafe['km between driver and passenger']==min_distance]
print(df_mesafe)

        


# In[ ]:




