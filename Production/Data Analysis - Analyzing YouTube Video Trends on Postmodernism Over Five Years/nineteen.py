import requests

resp = requests.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
print(resp.status_code, len(resp.text))
print(resp.text[:100])
