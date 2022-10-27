import json, keyword

class SimpleAdvert:
    def __init__(self, d):
        for i in d:
            if not isinstance(d[i], dict):
                setattr(self, i, d[i])
            else:
                setattr(self, i, SimpleAdvert(d[i]))

class ColorizeMixin:
    def color_output(self, s, color):
        return f"\033[1;{color};40m" + s


class Advert(ColorizeMixin):
    repr_color_code = 33

    def __init__(self, d):
        for i in d:
            if keyword.iskeyword(i):
                val = i + '_'
            else:
                val = i
            if not isinstance(d[i], dict):
                setattr(self, val, d[i])
            else:
                setattr(self, val, SimpleAdvert(d[i]))

        if 'price' not in d:
            self.price = 0
        elif self.price < 0:
            raise ValueError("price must be >= 0")

    def __repr__(self):
        return self.color_output(f'{self.title} | {self.price} ₽', self.repr_color_code)


if __name__ == '__main__':
    lesson_str = """{
    "title": "python",
    "price": 0,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    lesson = json.loads(lesson_str)
    lesson = Advert(lesson)
    print(lesson)
    print(lesson.price)
    print(lesson.location.address)
    corgi = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""
    corgi = json.loads(corgi)
    corgi = Advert(corgi)
    print(corgi)
    print(corgi.class_)
