import requests

instances = [
    'https://invidious.fdn.fr',
    'https://invidious.io',
    'https://yewtu.be',
    'https://inv.riverside.rocks',
    'https://invidious.snarl.pw',
    'https://invidious.weblibre.org',
    'https://invidious.lunar.icu',
    'https://invidious.privacyredirect.com',
    'https://invidious.nerdvpn.de',
    'https://invidious.mutahar.rocks',
    'https://invidious.namazso.eu',
    'https://invidious.projectsegfau.lt',
    'https://invidious.slipfox.xyz'
]

def test_instance(url):
    try:
        resp = requests.get(url + '/api/v1/stats', timeout=10)
        return resp.status_code, resp.headers.get('content-type'), resp.text[:200]
    except Exception as e:
        return str(e)

results = {url: test_instance(url) for url in instances}
print(results)
