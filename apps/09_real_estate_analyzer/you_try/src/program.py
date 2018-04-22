#!/usr/bin/env python
import csv
import os
import statistics

from data_types import Purchase


def main():
    print_header()
    file = get_data_file()
    data = load_file(file)
    query_data(data)


def print_header():
    print('----------------------------------------------------------------')
    print('                        REAL ESTATE APP')
    print('----------------------------------------------------------------')
    print()


def get_data_file():
    cur_dir = os.path.dirname(__file__)
    data_file = os.path.join(cur_dir, '..', 'data', 'SacramentoRealEstateTransactions2008.csv')
    return os.path.abspath(data_file)


def load_file(file):
    with open(file, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            purchases.append(Purchase.create_from_dict(row))
        return purchases


def query_data(data):

    data.sort(key=lambda p: p.price)

    print('The most expensive house: ${:,} with {} beds and {} baths'.format(data[-1].price, data[-1].beds, data[-1].baths))
    print('The least expensive house: ${:,} with {} beds and {} baths'.format(data[0].price, data[0].beds, data[0].baths))

    # average price house
    prices = []
    for p in data:
        prices.append(p.price)

    avg_price = statistics.mean(prices)
    print('The average house price is ${:,}'.format(int(avg_price)))

    # average price of 2 bedroom house
    prices = []
    for p in data:
        if p.beds == 2:
            prices.append(p.price)

    avg_price = statistics.mean(prices)
    print('The average house price for 2 bedroom is ${:,}'.format(int(avg_price)))


if __name__ == '__main__':
    main()
