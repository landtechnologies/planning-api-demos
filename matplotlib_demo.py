# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen
import json
import matplotlib.pylab as plt
import numpy as np

# make request
request = Request(r'https://api.landinsight.io/v_beta/planning/'
                  r'planning-applications?radius=100&limit=15&'
                  r'location=-0.1080217%2C51.5912874/', headers={
                      'Content-Type': r'application/json',
                      'X-Api-Key': r'YOUR_API_KEY_HERE'
                   })
response_body = urlopen(request).read()

# extract lat and long from records
data = json.loads(response_body)
locations = np.empty((len(data), 2))
for ii, record in enumerate(data):
    locations[ii,:] = record['location']['coordinates']
    
# plot as points
plt.plot(locations[:, 0], locations[:, 1], '.')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
plt.axes().set_aspect('equal', 'datalim')

