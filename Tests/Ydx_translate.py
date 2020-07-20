import requests

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'


def translate_text(mytext):

    params = {
        "key": KEY,
        "text": mytext,
        "lang": 'en-ru'
    }
    response = requests.get(URL, params=params)
    return response.json()


if __name__ == "__main__":

    json = translate_text("Hello")
    print(''.join(json['text']))
