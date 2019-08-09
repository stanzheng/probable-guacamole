import json
import github
import urllib.parse

DEFAULT_PAGE_SIZE = 30


def pretty_print(d): return json.dumps(d, indent=4, sort_keys=True)

def get_page_size(search):
    ar = search.split('~')
    if len(ar) > 1:
        return ar[1].split('page_size=')[1]
    else:
        return DEFAULT_PAGE_SIZE


def main():
    while (True):
        print("option flags, specify page size: ~page_size=50")
        search = input('Please Enter a Search Term or type `:q` to quit: ')
        # validate input
        if len(search)==0:
            continue
        per_page = get_page_size(search) 
        push_mode = input('Push Mode On? Y/N - (CTR+C to exit): ')
        print(search, urllib.parse.quote(search))
        if push_mode.lower() == 'y':
            print('Starting Unlimited Streaming for: {}'.format(search))
            page_counter = 1
            while True:
                pretty_print(github.search_repositories(search, per_page, page=page_counter, counter=0))
                page_counter +=1
                github.rate_limit_queue(10) # Rate limits by one query per set seconds
        else:
            pretty_print(github.search_repositories(search, per_page))
        if search == ':q':
            break
    print('Goodbye!')


if __name__ == "__main__":
    fail_execution = 0
    try: 
        main()
    except:
        fail_execution += 1 
        main()