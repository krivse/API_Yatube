# API_yatube

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
### Построение RESTful API для Yatube

Проект-продолжение проекта Yatube - блога, к которому создали API для обработки запросов к нему. В данном проекте рассматриваются виды запросов: GET, POST, PATCH, PUT, DELETE

Обработка всех видов запросов для постов (получить, изменить, удалить, создать), для 3-х  последних требуется специальные *permissions*:

- Обработка запросов для комментариев

- Обработка запросов для отслеживаемых авторов конкретного пользователя

- Обработка запросов для групп

К данному проекту прикручена документация в пакете static, при запуске проекта (runserver), чтобы с ней ознакомиться нужно перейти по адресу http://127.0.0.1/redoc.


### Как запустить проект:

#### Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:krivse/API_Yatube.git
```

#### Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

#### Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

#### Выполнить миграции:

```
python3 manage.py migrate
```

#### Запустить проект:

```
python3 manage.py runserver
```

###### Автор - Иван Красников, 2022
