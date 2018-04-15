import os
import sys

# TODO: should be a class to manage its own state


def load(name):
    """
    This method creates and loads a journal by name.

    :param name: The name of the journal.
    :return: A journal data structure populated with data
    """
    data = []
    filename = entries_path(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, data):
    filename = entries_path(name)

    with open(filename, 'w') as fout:
        for entry in data:
            fout.write(entry + '\n')


def entries_path(name):
    return os.path.join(sys.path[0], '..', 'entries', name + '.jrl')


def add_entry(text, data):
    data.append(text)
