import os 
import json

import asyncio
import aiohttp
from aiohttp_requests import requests

GITHUB_USER = os.environ.get('GITHUB_USER')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_BASE_URL= 'https://api.github.com/search/'


async def query_repositories(query):
    """
    ref: https://developer.github.com/v3/search/#search-repositories
    """
    response = await requests.get(f'{GITHUB_BASE_URL}repositories', auth=aiohttp.BasicAuth(GITHUB_USER, GITHUB_TOKEN), params={'q': query})
    text = await response.text()
    json = await response.json()
    return response, text, json


if __name__ == "__main__":    
    loop = asyncio.get_event_loop()
    r, text, res = loop.run_until_complete(query_repositories("foo"))
    print(r.get_encoding(), json.dumps(res, indent=4, sort_keys=True))