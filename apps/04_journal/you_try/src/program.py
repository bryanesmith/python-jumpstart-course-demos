#!/usr/bin/env python3

import journal


def main():
    print_header()
    event_loop()


def print_header():
    print('------------------------------------------------------')
    print('                      JOURNAL')
    print('------------------------------------------------------')
    print()


def event_loop():

    name = input("What's your journal's name?: ")
    entries = journal.load(name)

    print()
    print('What do you want to do?')
    cmd = None

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd entry, E[x]it: ').lower().strip()

        if cmd == 'l':
            list_entries(entries)
        elif cmd == 'a':
            add_entry(entries)
        elif cmd != 'x' and cmd:
            print('Unrecognized input: {}'.format(cmd))

        if cmd != 'x':
            print()

    journal.save(name, entries)
    print('Goodbye.')


def list_entries(entries):
    for idx, entry in enumerate(reversed(entries)):
        print('{}. {}'.format(idx + 1, entry))


def add_entry(entries):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, entries)


if __name__ == '__main__':
    main()