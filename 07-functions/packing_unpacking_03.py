# pass function as parameter
def calc_final_price(gross_price, tax, **params):
    return gross_price + gross_price * tax(**params)


def tax_x(imported):
    return 0.22 if imported else 0.13


def tax_y(explosive, factor=1):
    return 0.11 * factor if explosive else 0


if __name__ == '__main__':
    gross_price = 134.98
    final_price = calc_final_price(gross_price, tax_x, imported=True)
    final_price = calc_final_price(
        final_price, tax_y, explosive=True, factor=1.5)
    print(final_price)
