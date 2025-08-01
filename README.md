# Task Manager Monorepo

Монорепозиторий для управления задачами с микросервисной архитектурой.

## 🏗️ Архитектура

```
testbackdoor/
├── apps/                          # Микросервисы
│   ├── task-manager/             # Управление задачами
│   ├── user-management/          # Управление пользователями (планируется)
│   └── notification-service/     # Сервис уведомлений (планируется)
├── shared/                       # Общие компоненты
│   ├── database/                # Конфигурация БД
│   ├── auth/                    # Аутентификация
│   └── utils/                   # Общие утилиты
├── docker/                      # Docker конфигурация
├── docs/                        # Документация
└── scripts/                     # Скрипты развертывания
```

## 🚀 Быстрый старт

### Локальная разработка

1. **Клонирование репозитория:**
```bash
git clone https://github.com/PShlyundin/testbackdoor.git
cd testbackdoor
```

2. **Установка зависимостей:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. **Запуск приложения:**
```bash
python main.py
```

### Docker

```bash
# Запуск всех сервисов
docker-compose up -d

# Запуск только с PostgreSQL (production)
docker-compose --profile production up -d
```

## 📡 API Endpoints

### Основные эндпоинты
- `GET /` - Информация о монорепозитории
- `GET /health` - Проверка здоровья сервисов

### Task Manager API
- `GET /tasks/` - Получить все задачи
- `POST /tasks/` - Создать задачу
- `GET /tasks/{id}` - Получить задачу по ID
- `PUT /tasks/{id}` - Обновить задачу
- `DELETE /tasks/{id}` - Удалить задачу
- `PATCH /tasks/{id}/complete` - Отметить как выполненную
- `PATCH /tasks/{id}/incomplete` - Отметить как не выполненную

## 🔧 Разработка

### Структура микросервисов

Каждый микросервис в папке `apps/` имеет следующую структуру:
```
service-name/
├── main.py          # FastAPI приложение
├── models.py        # SQLAlchemy модели
├── schemas.py       # Pydantic схемы
├── crud.py          # CRUD операции
└── tests/           # Тесты
```

### Добавление нового микросервиса

1. Создайте папку в `apps/`
2. Создайте FastAPI приложение
3. Добавьте импорт в `main.py`
4. Смонтируйте приложение

### Общие компоненты

Используйте компоненты из `shared/` для переиспользования кода:
- `shared/database/` - Конфигурация базы данных
- `shared/utils/` - Общие утилиты
- `shared/auth/` - Аутентификация (планируется)

## 🐳 Docker

### Сборка образа
```bash
docker build -f docker/Dockerfile -t task-manager-monorepo .
```

### Запуск контейнера
```bash
docker run -p 8000:8000 task-manager-monorepo
```

## 📊 Мониторинг

- **Health Check:** `GET /health`
- **API Documentation:** `GET /docs`
- **Alternative Docs:** `GET /redoc`

## 🔗 Внешние зависимости

Монорепозиторий использует следующие внешние репозитории:

### Shared FastAPI Core
```
https://github.com/PShlyundin/shared-fastapi-core
```
Содержит общие компоненты: база данных, аутентификация, утилиты.

**Установка:**
```bash
pip install git+https://github.com/PShlyundin/shared-fastapi-core.git
```

### Task Management API
```
https://github.com/PShlyundin/task-management-api
```
Отдельный репозиторий только для управления задачами.

**Установка:**
```bash
git clone https://github.com/PShlyundin/task-management-api.git
cd task-management-api
pip install -r requirements.txt
```

## 🔄 Обновление зависимостей

```bash
# Обновить shared-fastapi-core
pip install --upgrade git+https://github.com/PShlyundin/shared-fastapi-core.git
```

## 📝 Лицензия

MIT License