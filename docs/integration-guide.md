# Руководство по интеграции внешних репозиториев

## 🎯 Обзор

Монорепозиторий теперь использует внешние репозитории для переиспользования компонентов:

- **[shared-fastapi-core](https://github.com/PShlyundin/shared-fastapi-core)** - Общие компоненты
- **[task-management-api](https://github.com/PShlyundin/task-management-api)** - Готовое приложение

## 📦 Установка зависимостей

### В монорепозитории
```bash
# Установка всех зависимостей включая shared-fastapi-core
pip install -r requirements.txt
```

### В отдельных проектах
```bash
# Установка только shared-fastapi-core
pip install git+https://github.com/PShlyundin/shared-fastapi-core.git

# Или клонирование task-management-api
git clone https://github.com/PShlyundin/task-management-api.git
cd task-management-api
pip install -r requirements.txt
```

## 🔧 Использование shared-fastapi-core

### Импорт компонентов
```python
# База данных
from shared_fastapi_core.database import Base, get_db, engine, SessionLocal

# Утилиты для ответов
from shared_fastapi_core.utils.response import (
    create_success_response,
    create_error_response,
    not_found_error,
    validation_error
)
```

### Пример использования
```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from shared_fastapi_core.database import get_db, Base, engine
from shared_fastapi_core.utils.response import create_success_response

app = FastAPI()

# Создание таблиц
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return create_success_response({"message": "Hello World"})
```

## 🔄 Обновление зависимостей

### Обновление shared-fastapi-core
```bash
pip install --upgrade git+https://github.com/PShlyundin/shared-fastapi-core.git
```

### Обновление task-management-api
```bash
cd task-management-api
git pull origin main
pip install -r requirements.txt
```

## 🏗️ Архитектура

### Монорепозиторий
```
testbackdoor/
├── apps/
│   └── task-manager/          # Использует shared-fastapi-core
├── shared/                    # Локальные компоненты (если нужны)
├── requirements.txt           # Включает shared-fastapi-core
└── main.py                   # Основное приложение
```

### Отдельные репозитории
```
shared-fastapi-core/
├── shared_fastapi_core/
│   ├── database/             # База данных
│   ├── utils/                # Утилиты
│   └── auth/                 # Аутентификация
└── setup.py                  # Установка пакета

task-management-api/
├── app/                      # Логика приложения
├── main.py                   # Точка входа
└── requirements.txt          # Зависимости
```

## 📝 Примеры интеграции

### Создание нового микросервиса
```python
# requirements.txt
fastapi>=0.104.1
git+https://github.com/PShlyundin/shared-fastapi-core.git

# main.py
from fastapi import FastAPI
from shared_fastapi_core.database import get_db
from shared_fastapi_core.utils.response import create_success_response

app = FastAPI()

@app.get("/")
def read_root():
    return create_success_response({"message": "New microservice"})
```

### Использование в существующем проекте
```bash
# Добавить в requirements.txt
git+https://github.com/PShlyundin/shared-fastapi-core.git

# Установить
pip install -r requirements.txt

# Использовать в коде
from shared_fastapi_core.database import Base, get_db
```

## 🚀 Развертывание

### Локальная разработка
```bash
# Монорепозиторий
python main.py

# Отдельное приложение
cd task-management-api
python main.py
```

### Docker
```bash
# Монорепозиторий
docker-compose up -d

# Отдельное приложение
docker build -t task-management-api .
docker run -p 8000:8000 task-management-api
```

## 🔍 Отладка

### Проверка установки
```python
# Проверить импорт
python -c "from shared_fastapi_core.database import Base; print('OK')"
```

### Обновление кэша pip
```bash
pip cache purge
pip install --no-cache-dir git+https://github.com/PShlyundin/shared-fastapi-core.git
```

## 📚 Дополнительные ресурсы

- [shared-fastapi-core](https://github.com/PShlyundin/shared-fastapi-core) - Документация библиотеки
- [task-management-api](https://github.com/PShlyundin/task-management-api) - Пример использования
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Официальная документация 