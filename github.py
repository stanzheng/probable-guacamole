import os 
import asyncio

import aiohttp
from aiohttp_requests import requests

GITHUB_USER = os.environ.get('GITHUB_USER')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')



async def query_user(query):
     response = await requests.get('https://api.github.com/search/repositories', auth=aiohttp.BasicAuth(GITHUB_USER, GITHUB_TOKEN), params={'query': query})
     text = await response.text()
     json = await response.json()
     return response, text, json


if __name__ == "__main__":    
    loop = asyncio.get_event_loop()
    r, text, json = loop.run_until_complete(query_user("foo"))
    print(r.get_encoding(), json)