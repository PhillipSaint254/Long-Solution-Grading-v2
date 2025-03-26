import requests

resp = requests.get('https://returnyoutubedislikeapi.com/votes', params={'videoId': '5D86_ptqd8I'})
print(resp.status_code)
print(resp.json())
