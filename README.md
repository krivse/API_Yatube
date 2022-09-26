# API_yatube

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)  ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)  ![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)  ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

# Построение RESTful API для Yatube

### Описание
Продолжение проекта Yatube - блога, к которому создали API для обработки запросов. В данном проекте рассматриваются виды запросов: GET, POST, PATCH, PUT, DELETE

### Функционал

- Подписка и отписка от авторизованного пользователя;

- Авторизованный пользователь просматривает посты, создавёт новые, удаляет и изменяет их;

- Просмотр сообществ;

- Комментирование, просмотр, удаление и обновление комментариев;

- Фльтрация по полям.

Обработка всех видов запросов для постов (получить, изменить, удалить, создать), для 3-х  последних требуется специальные *permissions*:

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
# для OS Lunix и MacOS
source venv/bin/activate

# для OS Windows
source venv/Scripts/activate
```

#### Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

#### Выполнить миграции:

```
cd yatube
python3 manage.py makemigrations
python3 manage.py migrate
```

#### Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов

### Получение токена

Отправить POST-запрос на адрес `api/v1/jwt/create/` и передать 2 поля в `data`:

- `username` - логин пользователя.
- `password` - пароль пользователя.

### Создание поста

Отправить POST-запрос на адрес `api/v1/posts/` и передать обязательное поле `text`, в заголовке указать `Authorization:Bearer <токен>`.

Пример запроса:

```json
{
  "text": "testpost"
}
```
Пример ответа:

```json
{
  "id": 1,

  "author": "krivse",

  "text": "testpost",

  "pub_date": "2022-07-22T12:12:22.021094Z",

  "image": null,

  "group": null
}
```
### Комментирование поста пользователя

Отправить POST-запрос на адрес `api/v1/posts/{post_id}/comments/` и передать обязательные поля `post` и `text`, в заголовке указать `Authorization:Bearer <токен>`.

Пример запроса:
```json
{
  "post": 1,
  "text": "test"
}
```
Пример ответа:
```json
{
 "id": 1,
 "author": "krivse",
 "text": "test",
 "created": "2022-07-22T12:12:13.146875Z",
 "post": 1
}
```
## Ресурсы

`Документация проекта:` [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

`Удобная площадка для работы с запросамия:` [https://www.postman.com/](https://www.postman.com/)

###### Автор - Иван Красников, 2022
