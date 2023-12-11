"""
В этом задании вам нужно реализовать ручку, которая принимает на вход ник пользователя на Github,
а возвращает полное имя этого пользователя.

- имя пользователя вы узнаёте из урла
- используя АПИ Гитхаба, получите информацию об этом пользователе (это можно сделать тут: https://api.github.com/users/USERNAME)
- из ответа Гитхаба извлеките имя и верните его в теле ответа: `{"name": "Ilya Lebedev"}`
- если пользователя на Гитхабе нет, верните ответ с пустым телом и статусом 404
- если пользователь на Гитхабе есть, но имя у него не указано, верните None вместо имени
"""
import requests
from django.http import HttpResponse, HttpRequest


def fetch_name_from_github_view(request: HttpRequest, github_username: str) -> HttpResponse:
    data = requests.get(f'https://api.github.com/users/{github_username}').json()
    if data.get('message') == 'Not Found':
        return HttpResponse(status=404)
    elif data['name']:
        return HttpResponse(data['name'])
    else:
        return HttpResponse('None')
