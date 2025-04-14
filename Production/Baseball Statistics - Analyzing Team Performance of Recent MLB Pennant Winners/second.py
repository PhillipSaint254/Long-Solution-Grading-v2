import requests

def fetch_stat(team_id, season, group, stat_field):
    url = f"https://statsapi.mlb.com/api/v1/teams/{team_id}/stats?stats=season&season={season}&group={group}"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    try:
        val = data['stats'][0]['splits'][0]['stat'][stat_field]
    except Exception as e:
        print(f"Error for team {team_id}, season {season}, group {group}, field {stat_field}: {e}")
        val = None
    return val

if __name__ == "__main__":
    # fetch for one example
    print(fetch_stat(140, 2023, 'hitting', 'avg'))
