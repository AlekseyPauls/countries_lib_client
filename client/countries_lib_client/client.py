import requests, json


def normalize_country_name(posname, dif_acc=0.7):
    url = 'http://127.0.0.1:5000/'
    params = {'posname': posname, 'dif_acc': dif_acc}
    r = requests.get(url, params=params)
    # Убираем кавычки
    return r.text[1:-2]


def match_country_name(key, value, priority=2):
    url = 'http://127.0.0.1:5000/'
    data = {'key': key, 'value': value, 'priority': priority}
    r = requests.post(url, data=data)
    return r.text


def del_country_name(key):
    url = 'http://127.0.0.1:5000/'
    data = {'key': key, 'value': 'DELETE', 'priority': ''}
    r = requests.post(url, data=data)
    return r.text
