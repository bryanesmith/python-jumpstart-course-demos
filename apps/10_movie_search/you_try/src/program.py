#!/usr/bin/env python
import requests

import movie_svc


def main():
    print_header()
    search_event_loop()


def print_header():
    print('---------------------------------------------------------')
    print('                     MOVIE SEARCH')
    print('---------------------------------------------------------')
    print()


def search_event_loop():
    search = None
    while search != 'x':
        try:
            search = input('Move search text (x to exit): ')
            if search != 'x':
                results = movie_svc.find_movies(search)
                print('Found {} results'.format(len(results)))
                for r in results:
                    print('{} -- {}'.format(r.year, r.title))
        except requests.exceptions.ConnectionError:
            print('Internet unavailable, please try again later.')
        except ValueError:
            print('Search text is required.')
        print()


if __name__ == '__main__':
    main()
