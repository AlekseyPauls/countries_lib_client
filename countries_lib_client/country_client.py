# -*- coding: utf-8 -*-
import requests, json


def normalize_country_name(url, posname, dif_acc=0.7):
    params = {'posname': posname, 'dif_acc': dif_acc}
    r = requests.get(url, params=params)
    # Убираем кавычки
    return r.text[1:-2]


def match_country_name(url, key, value, priority=2):
    data = {'key': key, 'value': value, 'priority': priority}
    r = requests.post(url, data=data)
    return r.text[1:-2]


def del_country_name(url, key):
    data = {'key': key, 'value': 'DELETE', 'priority': 1}
    r = requests.post(url, data=data)
    return r.text[1:-2]

if __name__ == '__main__':
    print(normalize_country_name('http://0.0.0.0:5000/', 'Rusia!!!!!'))