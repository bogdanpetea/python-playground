import requests

params = {
    'symbol':'TLV',
    'dt':'INTRA',
    'p':'intraday_60' ,
    'ajust':'1',
    'from':'1644515601',
    'to':'1645206801'
}

headers = {
    'Referer': 'https://www.bvb.ro/',
}

response = requests.get('https://wapi.bvb.ro/api/history', headers=headers, params=params)
print(response.json())