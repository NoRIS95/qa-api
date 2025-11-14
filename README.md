# QA-API
## О проекте
Этот бэкэнд-сервер предоставляет API для работы с вопросами и ответами:

**/questions** - Для вопросов:
- Добавление вопроса
- Отображение все вопросов
- Отображение конеретного вопроса по его id
- Удаление вопроса

**/answers** - Для ответов:
- Добавление ответа к вопросу
- Отображение конкретного ответа
- Удаление ответа

## Стек
 - Python 3.12
 - FastAPI
 - SQLAlchemy
 - PostgreSQL
 - Docker Compose
 - Make

### Инструкция по общей подготовке к запуску бэкенд-сервера (обязательна):
1. Клонируем репозиторий с сайта GitHub и заходим в директорию с проектом:
```
git clone https://github.com/NoRIS95/qa-api.git
cd qa-api

```
2. Копируем шаблон .env .и вписываем необходимые данные:
```
cp .env.template .env
```
3. Вставляем необходимые данные в файл .env:
```
POSTGRES_DB=<название базы данных>
POSTGRES_USER=<имя пользователя PostgreSQL>
POSTGRES_PASSWORD=<пароль пользователя PostgreSQL>
POSTGRES_HOST=postgres
SQLALCHEMY_DATABASE_URL=<ссылка на базу данных PostgreSQL, где в качестве хоста указан postgres>
```

### Инструкция к запуску проекта с помощью Docker Compose и Makefile:
1. Создаём контейнер и запускаем его в фоновом режиме
```
make app
```

### Команды Make:
* Создание файла миграции:
```
migrations
```
* Применение миграции к базе данных:
```
migrations
```
* Запуск через Docker Compose:
```
make app
```
* Остановка через Docker Compose:
```
make down
```
* Проверка линтеров:
```
make lint
```
* Починка линтеров:
```
make lint-fix
```
* Запуск всех тестов:
```
make test
```
* Запуск юнит тестов:
```
make test-unit
```
* Запуск интеграционных тестов:
```
make test-integ
```


## REST API

### Questions API
#### Отображение всех вопросов
```GET /questions/```

#### Добавление вопроса
```POST /questions/```
Параметры:
* text - текст вопроса

#### Отображение конкретного вопроса
```GET /questions/{id}```
Параметры:
* id - id вопроса

#### Удаление вопроса
```DELETE /questions/{id}```
Параметры:
* id - id вопроса

### Answers API
#### Добавление ответа к вопросу
```POST /questions/{id}/answers/ ```
Параметры:
* question_id - id вопроса
* text - текст ответа

#### Отображение ответа
```GET /answers/{id}```
Параметры:
* id - id ответа

#### Удаление вопроса
```DELETE /answers/{id}```
Параметры:
* id - id ответа