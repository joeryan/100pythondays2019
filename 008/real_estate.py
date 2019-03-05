import csv
from purchase import Purchase


def load_file(filename):
    purchases = []
    with open(filename, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)
    return purchases


def print_header():
    print('-'*50)
    print('         Real Estate Data')
    print('-'*50)


def main():
    print_header()
    data_file = 'SacramentoRealEstateTransactions2008.csv'
    homes = load_file(data_file)
    homes.sort(key=lambda p: p.price)
    # print highest priced home
    print("The highest priced home was ${:,}".format(homes[-1].price))
    # print lowest priced home
    print("The lowest priced home was ${:,}".format(homes[0].price))
    # print average home price
    # print average price for a 2-bedroom home


if __name__ == '__main__':
    main()