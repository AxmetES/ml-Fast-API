### Description
Учебный проект для работ с мл-моделью на FastAPI.

### Установка и запуск
1. Клонируйте репозиторий:
   ```bash
   git clone <git@github.com:AxmetES/ml-Fast-API.git>
   cd <ml-Fast-API>
   ```
2. Запустите докер контейнер:
   ```bash
   docker-compose up --build
   ```
### Использование
1. Приложение будет доступно по адресу: `http://localhost:8080`
2. Пример запроса:
```http
    POST http://localhost:8080/predict
    Content-Type: application/json
```
```
    {
      "row": {
        "Age": 35.0,
        "BusinessTravel": "Travel_Frequently",
        ....
        "YearsSinceLastPromotion": 2.0,
        "YearsWithCurrManager": 2.0
      }
    }
```

