#!/usr/bin/env python
import os
import platform
import subprocess

import cat_service

cat_count = 8


def main():
    print_header()
    path = get_or_create_output_folder()
    download_cats(path)
    display_cats(path)


def print_header():
    print('---------------------------------------------------')
    print('                   CAT FACTORY')
    print('---------------------------------------------------')
    print()


def get_or_create_output_folder():
    path = os.path.join(os.path.dirname(__file__), 'cat_pictures')

    if not os.path.exists(path):
        os.mkdir(path)

    return path


def download_cats(folder):
    for i in range(1, cat_count+1):
        cat_service.get_cat(folder, 'lolcat-{}'.format(i))


def display_cats(path):
    if platform.system() == 'Darwin':
        subprocess.call(['open', path])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', path])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', path])
    else:
        print('Files available: {}'.format(path))


if __name__ == '__main__':
    main()
