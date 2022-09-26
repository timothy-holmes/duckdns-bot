import json
import os.path

import requests

from src.logger import build_logger


def main():
    logger_name = ".".join(["duckdns-bot", __name__]) 
    logger = build_logger(logger_name)
    logger.debug("Created {logger_name} logger")

    with open("./config/config.json", "r") as c:
        config = json.load(c)
    logger.debug("Loaded config file")

    with open("./config/auth.secret.json", "r") as a:
        auth = json.load(a)
    logger.debug("Loaded auth file")

    if os.path.exists(x):
        with open("./data/current_ip.txt", "r") as i:
            old_ip = i.read().split('\n')[0]
        logger.debug(f"Current {ip=}")
    else:
        old_ip = ""
        logger.debug(f"No current_ip file found")

    dd_params = {
        'domains': ','.join(auth['DOMAINS']),
        'token': auth['TOKEN'],
        'verbose': config['DEBUG']
    }

    try:
        r_dd = requests.get("https://www.duckdns.org/update", params=params)
    except Exception as e:
        logger.error(f"Error while updating: {e}")
        raise e

    if config['DEBUG']:
        logger.debug(f"DuckDNS update: {r_dd.status_code} {r_dd.text.replace('\n',',')}")


if __name__ == "__main__":
    main()
