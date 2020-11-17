# Polls Application

1. Исходный код
<a href="https://github.com/antoshkoo/drf_polls">https://github.com/antoshkoo/drf_polls</a>

2. Для запуска локально необходимо в виртуальном окружении установить все необходимые пакеты. Для этого в терминале прописать:
```code
pip install -r requirements.txt
```

3. Работа с приложением
```code
http://127.0.0.1:8000/
```

4. Работа с панелью администратора:
Создание, редактирование, удаление опросов и вопросов к ним. Данные для входа в панель администратора: 
```code
http://127.0.0.1:8000/admin/ (admin:admin)
```

Добавление, изменение, редактирование опросов:
```code
http://127.0.0.1:8000/admin/polls/poll/
```

Добавление, изменение, редактирование вопросов:
```code
http://127.0.0.1:8000/admin/polls/pollsquestion/
```

Добавление, изменение, редактирование ответов:
```code
http://127.0.0.1:8000/admin/polls/pollsanswers/
```

## API
API со списком всех опросов и вопросов к ним (используйте ?format=json в строке URL, что бы получить данные json):
```link
Allow: GET, HEAD, OPTIONS
http://127.0.0.1:8000/api/v1/polls/all/
```

API с деталитзацией определенного опроса
```link
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
http://127.0.0.1:8000/api/v1/polls/poll/detail/1
```
