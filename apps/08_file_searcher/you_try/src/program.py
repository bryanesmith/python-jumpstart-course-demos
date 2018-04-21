#!/usr/bin/env python
import glob
import os
import collections

SearchResults = collections.namedtuple('SearchResults', 'file, line, text')


def main():
    print_header()

    folder = get_folder()
    if not folder:
        exit(1)

    text = get_search_text()
    if not text:
        exit(2)

    matches = search_folder(folder, text)

    print()
    for match in matches:
        print_match(match)


def print_match(match):
    print('---------- match ----------')
    print('file: ' + match.file)
    print('line: {}'.format(match.line))
    print('matching text:\n\t' + match.text.strip())
    print()


def print_header():
    print('--------------------------------------------------------')
    print('                         PyGrep')
    print('--------------------------------------------------------')
    print()


def get_folder():
    folder = input('Folder: ').strip()

    if not folder:
        print('No folder specified, bailing...')
        return None
    elif not os.path.isdir(folder):
        print('{} is not a directory, bailing...'.format(folder))
        return None
    else:
        return os.path.abspath(folder)


def get_search_text():
    text = input('Search text: ').strip()

    if not text:
        print('No search text, bailing...')
        return None
    else:
        return text


def search_folder(folder, search_text):
    items = glob.glob(os.path.join(folder, '*'))
    matches = []

    for item in items:
        path = os.path.join(folder, item)
        if os.path.isdir(path):
            yield from search_folder(path, search_text)
        else:
            yield from search_file(path, search_text)

    return matches


def search_file(file, search_text):
    with open(file, 'r', encoding='utf-8') as fin:
        line = 0
        try:
            for text in fin:
                line += 1
                if text.lower().find(search_text.lower()) >= 0:
                    sr = SearchResults(file=file, line=line, text=text)
                    yield sr
        except UnicodeDecodeError:
            pass  # skip 'Can't decode byte' errors for binary files


if __name__ == '__main__':
    main()
