# QA-API
## О проекте
Этот бэкенд-сервер предоставляет API для работы с вопросами и ответами:

**/questions** - Для вопросов:
- Добавление вопроса
- Отображение все вопросов
- Отображение конкретного вопроса по его id
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

### Инструкция по общей подготовке и запуску бэкенд-сервера с помощью Docker Compose и Makefile:
1. Склонируйте репозиторий с сайта GitHub и зайдите в директорию с проектом:
```
git clone https://github.com/NoRIS95/qa-api.git
cd qa-api

```
2. Скопируйте шаблон .env (настройки уже предзаполнены):
```
cp .env.example .env
```
3. При необходимости измените настройки в файле .env (опционально)

4. Создаём контейнер и запускаем его в фоновом режиме
```
make app
```

### Команды Make:
* Создание файла миграции:
```
make migrations NAME="название_миграции"
```
* Применение миграции к базе данных:
```
make migrate
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

## Доступ к API:
* Документация: http://localhost:8000/docs
* Health check: http://localhost:8000/health

## Примеры запросов
### Создание вопроса:
```bash
curl -X POST "http://localhost:8000/questions/" \
  -H "Content-Type: application/json" \
  -d '{"text": "Какой ваш любимый язык программирования?"}'
```

### Создание ответа:
```bash
curl -X POST "http://localhost:8000/questions/1/answers/" \
  -H "Content-Type: application/json" \
  -d '{"text": "Assembler", "user_id": "123e4567-e89b-12d3-a456-426614174000"}'
```