"""
webclip
"""

__author__ = "Brian Balsamo"
__email__ = "brian@brianbalsamo.com"
__version__ = "0.0.1"

from argparse import ArgumentParser
from os import environ
from redis import StrictRedis


def get_clipboard(redis_server, user):
    r = StrictRedis(host=redis_server)
    data = r.get(user)
    clipboard = data.decode("UTF-8")
    return clipboard


def set_clipboard(redis_server, user, x):
    r = StrictRedis(host=redis_server)
    r.set(user, x)


def main():
    parser = ArgumentParser()
    parser.add_argument("--copy", type=str, default=None)
    parser.add_argument("--paste", action='store_true')
    parser.add_argument("--user", default=None)
    parser.add_argument("--redis-server", type=str)

    args = parser.parse_args()

    # Try to get from the environment, if not supplied
    if args.user is None:
        args.user = environ.get('WEBCLIP_USER')
    if args.redis_server is None:
        args.redis_server = environ.get('WEBCLIP_REDIS_SERVER')

    # Test we have what we need
    if args.user is None:
        print("No User!")
        exit(1)
    if args.redis_server is None:
        print("No Server!")
        exit(1)
    if args.copy and args.paste:
        print("Pick one!")
        exit(1)

    # Do the stuff
    if args.paste:
        print(get_clipboard(args.redis_server, args.user))
        exit(0)
    if args.copy is not None:
        set_clipboard(args.redis_server, args.user, args.copy)
        exit(0)


if __name__ == '__main__':
    main()
