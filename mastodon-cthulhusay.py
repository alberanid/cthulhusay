#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import random
import cthulhusay
from mastodon import Mastodon

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)


def get_words_of_cthulhu():
    return cthulhusay.cthulhu_say(words=random.randint(1, 25))


def serve(api_url, token):
    words_of_cthulhu = get_words_of_cthulhu()
    print('serving:\n%s' % words_of_cthulhu)
    mastodon = Mastodon(access_token=token, api_base_url=api_url)
    mastodon.status_post(words_of_cthulhu)


if __name__ == '__main__':
    if 'CTHULHUBOT_TOKEN' not in os.environ:
        print("Please specify the Mastodon token in the CTHULHUBOT_TOKEN environment variable")
        sys.exit(1)
    if 'API_URL' not in os.environ:
        print("Please specify the Mastodon server in the API_URL environment variable")
        sys.exit(2)
    serve(api_url=os.environ['API_URL'], token=os.environ['CTHULHUBOT_TOKEN'])
