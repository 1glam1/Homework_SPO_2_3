FROM python:3.13-slim

WORKDIR /bot

COPY . /bot
RUN pip install pytelegrambotapi

CMD ["python","VladSPOBot.py"]