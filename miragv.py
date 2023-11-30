

import json
import requests

headers={}
headers["Authorization"] =""
headers["Content"] ="application/json"

getMissons_url= "http://mir.com/api/v2.0.0/missions"

response_getMissions =requests.get(getMissons_url,headers=headers)

print(response_getMissions)
print(response_getMissions.text)

#öppna json
missions=json.loads(response_getMissions.text)
print(missions[-1])




def runMission(missions, headers){

getMissons_url= "http://mir.com/api/v2.0.0/missions"

response_getMissions =requests.get(getMissons_url,headers=headers)

}


