from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

# get a movie
ep = ia.get_movie_episodes('6567314')
eps = ep["data"]["episodes"]

videos = []
import pdb;pdb.set_trace()
for s in eps.keys():
    for e in eps[s].keys():
        item = eps[s][e]
        videos.append({
            "episode": item['episode'],
            "id": f"tt6567314:{item['year']}:{item['episode']}",
            "title": item['title'],
            "season": item["year"]
        })

import pdb;pdb.set_trace()
