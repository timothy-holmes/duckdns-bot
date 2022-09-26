#!/bin/sh

# Start ping
curl -m 10 http://health.hh.home/ping/9cbf734d-20e8-4178-b59a-b7411747839f/start

# Payload here:
python /duckdns-bot/duckdns_bot.py

# Finished ping
curl -m 10 --retry 5 http://health.hh.home/ping/9cbf734d-20e8-4178-b59a-b7411747839f/$?
