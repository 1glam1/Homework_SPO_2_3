FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /bot

COPY . /bot 

# Устанавливаем зависимости
RUN pip install pytelegrambotapi

# Открываем порт, на котором будет работать приложение
EXPOSE 4200

# Запускаем приложение
CMD ["python","VladSPOBot.py"]
