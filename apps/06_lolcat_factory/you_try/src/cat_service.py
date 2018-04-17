import os
import shutil

import requests


def get_cat(folder, name):
    data = get_data_from_url('http://consuming-python-services-api.azurewebsites.net/cats/random')
    save_image(folder, name, data)


def get_data_from_url(url):
    return requests.get(url, stream=True).raw


def save_image(folder, name, data):
    file_name = os.path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)
