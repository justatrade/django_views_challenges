"""
В этом задании вам нужно реализовать вьюху, которая валидирует данные о пользователе.

- получите json из тела запроса
- проверьте, что данные удовлетворяют нужным требованиям
- если удовлетворяют, то верните ответ со статусом 200 и телом `{"is_valid": true}`
- если нет, то верните ответ со статусом 200 и телом `{"is_valid": false}`
- если в теле запроса невалидный json, вернуть bad request

Условия, которым должны удовлетворять данные:
- есть поле full_name, в нём хранится строка от 5 до 256 символов
- есть поле email, в нём хранится строка, похожая на емейл
- есть поле registered_from, в нём одно из двух значений: website или mobile_app
- поле age необязательное: может быть, а может не быть. Если есть, то в нём хранится целое число
- других полей нет

Для тестирования рекомендую использовать Postman.
Когда будете писать код, не забывайте о читаемости, поддерживаемости и модульности.
"""
import json

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse
from json import JSONDecodeError


def validate_user_data_view(request: HttpRequest) -> HttpResponse:
    # return HttpResponse((type(request.body), json.loads(request.body)))
    try:
        data = json.loads(request.body)
        validate_email(data['email'])
    except (JSONDecodeError, ValidationError):
        data = {}
    if data:
        if (5 < len(data['full_name']) < 256
                and data['email']
                and data['registered_from'] in ['website', 'mobile_app']
                and (
                        str(data.get('age')).isnumeric()
                        if data.get('age') else True
                )):
            return JsonResponse({"is_valid": True})
        else:
            return JsonResponse({"is_valid": False})
    else:
        return HttpResponseBadRequest('bad request')
