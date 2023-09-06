# DuckDNS Updater

Using a docker container (curl) to package config. Requires running instance of [ofelia](https://github.com/mcuadros/ofelia).

## Usage

Set IP addresses at [duckdns.org](https://duckdns.org/account) to 1.1.1.1 (or whatever) and copy token value.

```sh
git clone https://github.com/timothy-holmes/duckdns-bot && duckdns-bot
printf "TOKEN=<duckdns-token>\nDOMAIN1=<duckdns-subdomain>\n" > .env.secrets
nano docker-compose.yml # remove surplus labels, if necessary
docker-compose --env_file .env.secrets up -d
```

Remove surplus labels in docker-compose.yml before starting container.  After the expected time has passed, check for updated IP addresses.