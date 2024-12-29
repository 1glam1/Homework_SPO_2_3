# Домашнее задание по Системному программному обеспечению (СПО) №2
## Автор
Корпусев Владислав Дмитриевич
Группа: Фт-320007
## Программа
Телеграм-бот, который умеет генерировать случайное число или спрашивать "как дела?".
## Метод создания телеграм-бота
Телеграм-бот был написан на языке python при помощи библиотеки telebot.
Ее можно установить при помощи pip install pytelegrambotapi.
## Создание Dockerfile
```
# Используем официальный образ python
FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /bot

COPY . /bot 

# Устанавливаем зависимости
RUN pip install pytelegrambotapi

# Открываем порт, на котором будет работать приложение
EXPOSE 5000

# Запускаем приложение
CMD ["python","VladSPOBot.py"]
```
Запускаем терминал, переходим в корневую папку проекта `cd (путь до корневой папки с проектом)`.
Создаем образ, где 'telegram-bot' - это название: `docker build -t telegram-bot:1.0 ./`.

Готовый образ в разделе 'images':
![image](https://github.com/user-attachments/assets/22490d11-3e4c-42dd-b24a-344c95c1181d)
## Создание и запуск контейнера

Создаем и запускаем контейнер командой `docker run -p 8888:5000 telegram-bot`

`docker run` запускает контейнер, далее идет флаг `-p`, который принимает параметры [HOST_PORT]:[CONTAINER_PORT],
соответственно порт хоста, который мы как раз можем менять (нужно чтобы он был свободен) и порт контейнера,
на который будет пробрасываться.

После запуска контейнера можем открыть бота в телеграмме `@VladSPOBot`.

Я пользовался Docker Desktop, поэтому контейнер могу запускать оттуда.

Запущенный контейнер:
![image](https://github.com/user-attachments/assets/ca13c973-3ad8-4a9d-978d-7e33fb05f118)

Работа бота в телеграме:
![image](https://github.com/user-attachments/assets/47eecbf7-23cc-4aa4-8b9d-8f9d2b415e07)

Логи в Docker Desktop:
![image](https://github.com/user-attachments/assets/14dc9bde-2a60-4f08-80e9-c0e2aba428de)

Также в Docker Desktop можно посмотреть процент использования CPU и RAM. 
### Указывать порт и localhost в моем случае не нужно, так как страницы, на которую ведет порт, не существует.
## Загрузка бота на хостинг
В качестве хостинга был выбран Amvera Cloud.

Настраиваем конфигурационный файл и устанавливаем build. В нашем случае build - это Dockerfile:
![image](https://github.com/user-attachments/assets/107c7f82-a920-4c9b-be85-88be3533b28d)

Логи в Amvera Cloud:
![image](https://github.com/user-attachments/assets/7c4a2a60-0d93-436f-952e-90dfb6faac41)

## Код телеграм-бота (VladSPOBot.py) представлен в репозитории.


