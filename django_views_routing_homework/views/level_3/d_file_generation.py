"""
В этом задании вам нужно научиться генерировать текст заданной длинны и возвращать его в ответе в виде файла.

- ручка должна получать длину генерируемого текста из get-параметра length;
- дальше вы должны сгенерировать случайный текст заданной длины. Это можно сделать и руками
  и с помощью сторонних библиотек, например, faker или lorem;
- дальше вы должны вернуть этот текст, но не в ответе, а в виде файла;
- если параметр length не указан или слишком большой, верните пустой ответ со статусом 403

Вот пример ручки, которая возвращает csv-файл: https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
С текстовым всё похоже.

Для проверки используйте браузер: когда ручка правильно работает, при попытке зайти на неё, браузер должен
скачивать сгенерированный файл.
"""
import random
from django.http import HttpResponse, HttpRequest, HttpResponseForbidden


def generate_file_with_text_view(request: HttpRequest) -> HttpResponse:
    length = int(request.GET.get('length', '0'))
    if 1 > length or length > 10000:
        return HttpResponseForbidden()
    else:
        letters = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g',
                   8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
                   15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
                   21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z',
                   27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: '. ', 32: ', '}
        text = [letters[random.randint(1, 32)] for _ in range(length)]
        return HttpResponse(text,
                            content_type='text/plain',
                            headers={"Content-Disposition": 'attachment; filename="result.txt"'})
