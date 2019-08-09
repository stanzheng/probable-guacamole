import os 
import json
import queue

import asyncio
import aiohttp
from aiohttp_requests import requests

GITHUB_USER = os.environ.get('GITHUB_USER')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_BASE_URL= 'https://api.github.com/search/'

def pretty_print(d): return json.dumps(d, indent=4, sort_keys=True)

async def query_repositories(*args, **kwargs):
    """
    ref: https://developer.github.com/v3/search/#search-repositories
    """
    # print(args, kwargs)
    response = await requests.get(f'{GITHUB_BASE_URL}repositories', auth=aiohttp.BasicAuth(GITHUB_USER, GITHUB_TOKEN), params=args)
    text = await response.text()
    json = await response.json()
    return response, text, json

async def query_generic(URL, **args):
    response = await requests.get(URL, auth=aiohttp.BasicAuth(GITHUB_USER, GITHUB_TOKEN), params=args)
    text = await response.text()
    json = await response.json()
    return response, text, json

def parse_repositories(repositories):
    return [i.get('full_name') for i in repositories.get('items')]


def enqueue():
    """
    Python Queue job Queue
    """
    return None

if __name__ == "__main__":    
    loop = asyncio.get_event_loop()
    for i in range(2, 3):
        req, text, res = loop.run_until_complete(query_repositories({
            'q': 'foo',
            'per_page': 50,
            'page': i 
        }))
        print(req.headers, req.get_encoding(), parse_repositories(res), len(res['items']))
        import ipdb; ipdb.set_trace()