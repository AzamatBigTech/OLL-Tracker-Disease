# README.md
# ALL Disease Tracker Bot
Телеграм-бот для отслеживания информации о заболевании ALL с использованием Supabase.

# OLL Tracker (Disease)

Python-проект для трекинга данных (симптомы/состояние/заметки — по логике проекта) с хранением в Supabase (PostgreSQL).
В репозитории есть SQL-схема базы и конфигурация для деплоя.

## Features
- Добавление записей (дата/состояние/показатели)
- Просмотр истории / списка записей
- Хранение данных в Supabase (PostgreSQL)
- Инициализация базы через SQL-схему из репозитория
- (Опционально) деплой через конфиг в репозитории

## Tech stack
- Python
- Supabase (PostgreSQL)
- SQL schema
- Deploy: (Render / другое — укажи что используешь)

## How to run (locally)
```bash
git clone https://github.com/AzamatBigTech/OLL-Tracker-Disease.git
cd OLL-Tracker-Disease
python -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
