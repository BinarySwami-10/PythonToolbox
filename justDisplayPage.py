import requests

url = "https://mytest666-f468.restdb.io/rest/people"

headers = {
    'content-type': "application/json",
    'x-apikey': "e234f73576cedc04b8c2bf8d2f15a8840400c",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
                    