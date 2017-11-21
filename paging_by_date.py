# -*- coding: utf-8 -*-
from urllib2 import Request, urlopen
import json

# define a function that returns a batch of 100 results, sorted from newest to oldest
def getRecords(api_key, gss_code='E09000014', date_to=(2017,2,19)):
    # construct url
    url = (r'https://api.landinsight.io/v1/planning-applications'
              r'/search?gss_code={gss_code:}&limit=100&'
              r'title=approved&date_received_range_to={date_to:}&'
              r'sort=-date_received').format(
                  gss_code=gss_code,
                  date_to='-'.join(str(x) for x in date_to))
    request = Request(url, headers={
                          'Content-Type': r'application/json',
                          'X-Api-Key': api_key
                       })
    response_body = urlopen(request).read()
    # drop '_score' bit of results, just returning the array of data
    return [result['search_result'] for result in json.loads(response_body)]
   

API_KEY = r'___YOUR_API_KEY_HERE____'

results = []
earliest_date = ('2017', '2', '19')
for ii in range(3): 
    # get a batch of results that have a slightly earlier date_received than the previous batch
    print "getting 100 before date", earliest_date, "len(results)=", len(results)
    results += getRecords(API_KEY, date_to=earliest_date)
    earliest_date = results[-1]['date_received']
    earliest_date = (earliest_date[0:4], earliest_date[5:7],earliest_date[8:10])
    
# show some of the data obtained
for x in results:
   print (x['date_received'], x['title'])
   
