import requests
import json
#from pymongo import Connection,bson

def pull():
    r = requests.get("http://saccounty.cloudapi.junar.com/api/v2/datastreams/CRIME-DATA/data.json/?auth_key=f6fda8ad808a146c09b00118dc0b42f51875238f&limit=100&output=csv")
    
    '''
    with open('crime-data-100.txt', 'w') as outfile:
        json.dump(r.content, outfile)
    '''
    with open('crime-data-100.csv', 'w') as outfile:
        outfile.write(r.text)

#def mongodbInit():
pull()
