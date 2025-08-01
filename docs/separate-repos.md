# Отдельные репозитории для переиспользования

## 🎯 Цель

Создать отдельные репозитории для переиспользования компонентов в других проектах.

## 📦 Предлагаемые репозитории

### 1. **shared-fastapi-core**
```
https://github.com/PShlyundin/shared-fastapi-core
```

**Содержимое:**
- Общие компоненты базы данных
- Утилиты для ответов API
- Middleware компоненты
- Общие схемы и валидаторы

**Использование:**
```bash
pip install git+https://github.com/PShlyundin/shared-fastapi-core.git
```

### 2. **task-management-api**
```
https://github.com/PShlyundin/task-management-api
```

**Содержимое:**
- Полное приложение для управления задачами
- Готовая к развертыванию версия
- Документация и тесты

**Использование:**
```bash
git clone https://github.com/PShlyundin/task-management-api.git
cd task-management-api
pip install -r requirements.txt
python main.py
```

### 3. **fastapi-microservice-template**
```
https://github.com/PShlyundin/fastapi-microservice-template
```

**Содержимое:**
- Шаблон для создания новых микросервисов
- Базовая структура проекта
- CI/CD конфигурация

## 🔗 Ссылки между репозиториями

### В монорепозитории
```python
# Использование shared-fastapi-core
from shared.database import Base, get_db
from shared.utils.response import create_success_response
```

### В отдельных проектах
```python
# Установка shared-fastapi-core
pip install git+https://github.com/PShlyundin/shared-fastapi-core.git

# Использование
from shared_fastapi_core.database import Base, get_db
from shared_fastapi_core.utils.response import create_success_response
```

## 📋 План создания

### Этап 1: Shared FastAPI Core
1. Создать репозиторий `shared-fastapi-core`
2. Вынести общие компоненты из `shared/`
3. Создать setup.py для установки
4. Добавить документацию

### Этап 2: Task Management API
1. Создать репозиторий `task-management-api`
2. Скопировать `apps/task-manager/`
3. Добавить зависимости на shared-fastapi-core
4. Создать README и документацию

### Этап 3: Microservice Template
1. Создать репозиторий `fastapi-microservice-template`
2. Создать базовый шаблон
3. Добавить примеры использования
4. Настроить CI/CD

## 🔄 Обновление зависимостей

### В монорепозитории
```bash
# Обновить shared компоненты
git submodule update --remote

# Или использовать pip для внешних зависимостей
pip install --upgrade git+https://github.com/PShlyundin/shared-fastapi-core.git
```

### В отдельных проектах
```bash
# Обновить shared-fastapi-core
pip install --upgrade git+https://github.com/PShlyundin/shared-fastapi-core.git
```

## 📝 Примеры использования

### Создание нового микросервиса с shared-fastapi-core
```python
from fastapi import FastAPI
from shared_fastapi_core.database import Base, get_db
from shared_fastapi_core.utils.response import create_success_response

app = FastAPI()

@app.get("/")
def read_root():
    return create_success_response({"message": "Hello World"})
```

### Использование task-management-api
```bash
# Клонирование
git clone https://github.com/PShlyundin/task-management-api.git

# Установка зависимостей
pip install -r requirements.txt

# Запуск
python main.py
```

## 🎯 Преимущества

1. **Переиспользование кода** - общие компоненты доступны всем проектам
2. **Изоляция** - каждый репозиторий имеет свою ответственность
3. **Масштабируемость** - легко добавлять новые микросервисы
4. **Поддержка** - проще поддерживать отдельные компоненты
5. **Сообщество** - другие разработчики могут использовать ваши компоненты 