import os 
import time

import asyncio
import aiohttp
from aiohttp_requests import requests

import backoff

GITHUB_USER = os.environ.get('GITHUB_USER')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_BASE_URL= 'https://api.github.com/search/'
RATE_LIMIT_BACKOFF = 0
DEFAULT_PAGES_RETURNED = 2


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

def rate_limit_queue(backoff=0):
    """Provides a Fake Queue Backoff. *NOTE* This Blocks All Execution on Thread
    # @TODO Proper interface would be use the pypy package `backoff`
    # @TODO Proper interface would be use the queue with `timeout` attribute
    """
    if backoff == 0:
        return 
    time.sleep(backoff)
 
@backoff.on_exception(backoff.expo, Exception)
def search_repositories(query, per_page, page=1, counter=DEFAULT_PAGES_RETURNED):
    loop = asyncio.get_event_loop()
    print("Starting Requests... Page:{}".format(page))
    req, text, res = loop.run_until_complete(
        query_repositories({
        'q': query,
        'per_page': per_page,
        'page': page
    }))
    # debug string
    # print(req.headers, text, req.get_encoding(), parse_repositories(res))
    if counter != 0 and res['incomplete_results']== False:
        return parse_repositories(res) + search_repositories(query,per_page, page=page+1, counter=counter-1)
    else:
        return parse_repositories(res)

if __name__ == "__main__":    
    loop = asyncio.get_event_loop()
    query = 'foo'
    per_page = 50
    req, text, res = loop.run_until_complete(query_repositories({
        'q': query,
        'per_page': per_page
    }))
    rate_limit_queue(backoff=RATE_LIMIT_BACKOFF)
    for i in range(2, len(res['items'])):

        if i == 2:
            break
        rate_limit_queue(backoff=RATE_LIMIT_BACKOFF)
        print(req.headers, req.get_encoding(), parse_repositories(res))
        # import ipdb; ipdb.set_trace()