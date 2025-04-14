from second import fetch_stat
from first import get_teams

def get_records():
    teams = get_teams()
    records = []
    for team_name, season, team_id in teams:
        # hitting average
        avg = fetch_stat(team_id, season, 'hitting', 'avg')
        # ERA (pitching)
        era = fetch_stat(team_id, season, 'pitching', 'era')
        # fielding percentage
        fld = fetch_stat(team_id, season, 'fielding', 'fielding')
        # convert to floats
        try:
            avg_float = float(avg)
        except:
            # remove leading dot
            if isinstance(avg, str) and avg.startswith('.'):
                avg_float = float('0' + avg)
            else:
                avg_float = None
        try:
            era_float = float(era)
        except:
            if isinstance(era, str) and era.startswith('.'):
                era_float = float('0' + era)
            else:
                era_float = None
        try:
            fld_float = float(fld)
        except:
            if isinstance(fld, str) and fld.startswith('.'):
                fld_float = float('0' + fld)
            else:
                fld_float = None
        records.append({'Team': team_name, 'Season': season, 'BattingAverage': avg_float, 'ERA': era_float, 'FieldingPct': fld_float})
    return records

if __name__ == "__main__":
    print(get_records())
