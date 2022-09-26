from python:latest

ENV INSTALL_PATH /duckdns-bot
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install requirements.txt

COPY duckdns_bot.py duckdns_bot.py
COPY src src/

ENTRYPOINT ["bash"]
