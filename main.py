
DEFAULT_PAGE_SIZE = 30


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
        
        page_size = get_page_size(search) 
        if search == ':q':
            break
    print('Goodbye!')


if __name__ == "__main__":
    main()