import json
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

    params = {
        'domains': ','.join(auth['DOMAINS']),
        'token': auth['TOKEN'],
        'verbose': config.get('DUCKDNS_VERBOSE',None)
    }

    try:
        r_dd = requests.get(
            url = config["DUCKDNS_UPDATE_URL"], 
            params = {k: v for k,v in params if v}
        )
    except Exception as e:
        logger.error(f"Error while updating: {e}")
        raise e

    if config['DUCKDNS_VERBOSE']:
        logger.debug(f"DuckDNS update: {r_dd.status_code} {r_dd.text.replace('\n',', ')}")


if __name__ == "__main__":
    main()
