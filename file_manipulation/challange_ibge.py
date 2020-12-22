import csv
from urllib import request


def read(url):
    with request.urlopen(url) as inpt:
        print('Download CSV')
        data = inpt.read().decode('latin1')
        for city in csv.reader(data.splitlines()):
            print(f'{city[8]}: {city[3]}')

if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')