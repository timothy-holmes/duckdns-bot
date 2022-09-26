FROM python:latest

ENV INSTALL_PATH /duckdns-bot
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY duckdns_bot.py duckdns_bot.py
COPY src src/
COPY scripts scripts/
RUN chmod -R +x scripts

# start up run
RUN /duckdns-bot/scripts/run.sh

CMD tail -d
