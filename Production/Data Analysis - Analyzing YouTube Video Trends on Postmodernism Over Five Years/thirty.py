import requests

resp = requests.get('https://playboard.co/en/video/5D86_ptqd8I')
text = resp.text
# find the substring around 'Likes'
idx = text.find('Likes')
print(text[idx-100: idx+100])
