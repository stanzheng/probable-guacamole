import os 
import json
import queue

import asyncio
import aiohttp
from aiohttp_requests import requests

GITHUB_USER = os.environ.get('GITHUB_USER')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_BASE_URL= 'https://api.github.com/search/'

def pp(d): return json.dumps(d, indent=4, sort_keys=True)

async def query_repositories(params):
    """
    ref: https://developer.github.com/v3/search/#search-repositories
    """
    # print(args, kwargs)
    response = await requests.get(f'{GITHUB_BASE_URL}repositories', auth=aiohttp.BasicAuth(GITHUB_USER, GITHUB_TOKEN), params=params)
    text = await response.text()
    json = await response.json()
    return response, text, json

def parse_repositories(repositories):
    return [i.get('full_name') for i in repositories.get('items')]

async def query_generic(URL, **args):
    response = await requests.get(URL, auth=aiohttp.BasicAuth(GITHUB_USER, GITHUB_TOKEN), params=args)
    text = await response.text()
    json = await response.json()
    return response, text, json

if __name__ == "__main__":    
    loop = asyncio.get_event_loop()
    query = 'foo'
    per_page = 50
    req, text, res = loop.run_until_complete(query_repositories({
        'q': 'query,
        'per_page': per_page
    }))
    for i in range(2, len(res['items'])):

        if i == 2:
            break
        print(req.headers, req.get_encoding(), parse_repositories(res))
        import ipdb; ipdb.set_trace()