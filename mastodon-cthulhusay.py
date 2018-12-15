#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import random
import cthulhusay
from mastodon import Mastodon

API_URL = 'https://botsin.space/'

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)


def get_words_of_cthulhu():
    return cthulhusay.cthulhu_say(words=random.randint(1, 25))


def serve(token):
    words_of_cthulhu = get_words_of_cthulhu()
    print('serving:\n%s' % words_of_cthulhu)
    mastodon = Mastodon(access_token=token, api_base_url=API_URL)
    mastodon.status_post(words_of_cthulhu)


if __name__ == '__main__':
    if 'CTHULHUBOT_TOKEN' not in os.environ:
        print("Please specify the Mastodon token in the CTHULHUBOT_TOKEN environment variable")
        sys.exit(1)
    serve(token=os.environ['CTHULHUBOT_TOKEN'])
