import requests

def get_resp():
    url = 'https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2023-11/climate-transition-action-plan-roadmap.pdf'
    return requests.get(url)

if __name__ == "__main__":
    resp = get_resp()
    print(resp.status_code, len(resp.content))
