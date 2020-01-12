import json
import logging
youtube = json.loads(open("youtube/final.json").read())
streams = {"series": {}}


def search_youtube(ep):
    title = ep["title"]
    year = ep["year"]

    for item in youtube:
        if title in item["snippet"]["title"] and year in item["snippet"]["publishedAt"]:
            return item
    return None

multiple = 0
zero = 0

from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

# get a movie
ep = ia.get_movie_episodes('6567314')
eps = ep["data"]["episodes"]
import pdb;pdb.set_trace()
for s in eps.keys():
    for e in eps[s].keys():
        item = search_youtube(eps[s][e])

        if item == None:
            logging.warning(f"No video found for title: {eps[s][e]['title']}")
            zero = zero +1
            continue
        year = eps[s][e]["year"]
        id = f"tt6567314:{year}:{e}"
        videoId = item["snippet"]["resourceId"]["videoId"]
        streams["series"][id] = [{
            "title": "Youtube",
            "ytId": videoId
        }]

import pdb;pdb.set_trace()

