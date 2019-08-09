



def main():
    while (True):
        search = input('Please Enter a Search Term or type `:q` to quit: ')
        print(search)
        if search == ':q':
            break
    print('Goodbye!')


if __name__ == "__main__":
    main()