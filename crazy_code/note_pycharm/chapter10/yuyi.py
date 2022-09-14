import json
import requests

content_txt = json.dumps(
    {
        "text": "你是个好人"
    }
)

header = {
    'content-Type': 'application/json'
}

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=4ALYgf4HeVqWhUASGzOicaLH&client_secret=Avj3ItXKf9qisUDTYtn6gNYchbKvUdFG'
response = requests.get(host)
if response:
    print(response.json())

mytoken = response.json()['access_token']

url1 = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify"
myurl = url1 + "?charset=UTF-8&access_token=" + mytoken

result = requests.post(url=myurl, headers=header, data=content_txt).json()
print(result)

for item in result:
    print(item,':', result[item])
