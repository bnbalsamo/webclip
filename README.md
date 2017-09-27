# webclip

v0.0.1

[![Build Status](https://travis-ci.org/bnbalsamo/webclip.svg?branch=master)](https://travis-ci.org/bnbalsamo/webclip) [![Coverage Status](https://coveralls.io/repos/github/bnbalsamo/webclip/badge.svg?branch=master)](https://coveralls.io/github/bnbalsamo/webclip?branch=master)

Demo project for Docker for Developers talk. Clipboard as a service.

```
$ webclip --help
usage: webclip [-h] [--copy COPY] [--paste] [--user USER]
               [--redis-server REDIS_SERVER]

optional arguments:
  -h, --help            show this help message and exit
  --copy COPY
  --paste
  --user USER
  --redis-server REDIS_SERVER
```

## Environmental Variables
- WEBCLIP_USER: Checked for a username if ```--user``` isn't present
- WEBCLIP_REDIS_SERVER: Check for a server if ```--redis-server``` isn't present

# Author
Brian Balsamo <brian@brianbalsamo.com>
