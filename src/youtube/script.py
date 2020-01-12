# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import json
import requests
import logging

URL = "https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2Csnippet&maxResults=50&playlistId=UUzQUP1qoWDoEbmsQxvdjxgQ&alt=json&key="

def save(obj, number):
    with open(f"resp{number}.json", "w") as fd:
        fd.write(json.dumps(obj))
    logging.warn(f"File resp{number}.json")

def main():

    key = ""
    req = requests.get(URL + key)
    save(req.json()["items"], "1")
    nextPageToken = req.json().get("nextPageToken")
    
    counter = 1
    while nextPageToken is not None:
        req = requests.get(URL + key + "&pageToken=" + nextPageToken)
        counter = counter + 1
        save(req.json()["items"], str(counter))
        nextPageToken = req.json().get("nextPageToken")


if __name__ == "__main__":
    main()
