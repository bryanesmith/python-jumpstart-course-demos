import datetime


def print_header():
    print('----------------------------------------------')
    print('                BIRTHDAY APP')
    print('----------------------------------------------')


def get_birthday():
    print('When were you born?')

    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    return datetime.date(year, month, day)


def compute_days_between_dates(original, target):
    this_year = datetime.date(target.year, original.month, original.day)
    delta = this_year - target
    return delta.days


def print_birthday_info(days):
    if days < 0:
        print("Your birthday was {} days ago".format(-days))
    elif days > 0:
        print("Your birthday is in {} days".format(days))
    else:
        print("Happy birthday!!!")


def main():
    print_header()
    bday = get_birthday()
    days = compute_days_between_dates(bday, datetime.date.today())
    print_birthday_info(days)


main()
