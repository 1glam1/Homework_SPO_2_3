FROM python:3.13-slim

WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install pytelegrambotapi

CMD ["python","VladSPOBot.py"]
virtualisation.docker.extraPackages = [pkgs.openssh]
