from thirteen import get_desc_tano_episode

desc_tano_episode = get_desc_tano_episode()

if 'tano' in desc_tano_episode.description.lower():
    start_idx = desc_tano_episode.description.lower().index('tano')
    desc_tano_episode.description[start_idx-50:start_idx+60]

print(desc_tano_episode.description)
