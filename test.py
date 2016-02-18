import requests
import json


r = requests.get("http://saccounty.cloudapi.junar.com/api/v2/datastreams/SACRA-COUNT-CALIF-QUICK-FACTS/data.json/?auth_key=f6fda8ad808a146c09b00118dc0b42f51875238f")
with open('data.txt', 'w') as outfile:
    json.dump(r.content, outfile)

