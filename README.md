# Репозиторий для тестового задания

## Функционал

- **Древовидное меню**: Меню отображается с поддержкой иерархии (вложенные пункты).
- **Редактирование через админку**: Добавление и редактирование меню и его пунктов через стандартную админку Django.
- **Настройка отображения**: Активный пункт меню определяется по текущему URL. Меню можно отображать на любой странице с помощью шаблонного тега.
- **Многократное использование**: На одной странице может быть несколько меню, определяемых по их именам.
- **Эффективное использование**: Отрисовка каждого меню требует только одного запроса к базе данных.

## Установка

### Установите зависимости:
```bash
pip install -r requirements.txt
```
# Настройка проекта

### Примените миграции для создания необходимых таблиц в базе данных:

```bash
python manage.py migrate
```

### Создайте суперпользователя для доступа к админке:

```bash
python manage.py createsuperuser
```

### Запустите сервер разработки:
```bash
python manage.py runserver
```