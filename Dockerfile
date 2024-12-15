FROM python:3.13-slim

WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install pytelegrambotapi

CMD ["python","VladSPOBot.py"]
RUN eval `ssh-agent -s` && \
    ssh-add id_rsa && \
    git clone git@github.com:1glam1/Homework_SPO_2.git
