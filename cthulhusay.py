#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""R'lyehian language generator.  The one and only cthulhu-fhtagn-ator.

Copyright 2017 Davide Alberani <da@erlug.linux.it>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import random

# Summoned from https://www.yog-sothoth.com/wiki/index.php/R'lyehian
WORDS = ["'ai", "'bthnk", "'fhalma", 'ah', 'athg', 'bug', "ch'", 'chtenff', 'ebumna', 'ee', 'ehye', 'ep', 'fhtagn',
         "fm'latgh", 'ftaghu', 'geb', 'gnaiih', "gof'nn", 'goka', 'gotha', "grah'n", "hafh'drn", 'hai', 'hlirgh',
         'hrii', 'hupadgh', 'ilyaa', "k'yarnak", 'kadishtu', "kn'a", "li'hee", 'llll', 'lloig', "lw'nafh", "mnahn'",
         "n'gha", "n'ghft", 'nglui', "nilgh'ri", 'nog', 'nw', 'ooboshu', "orr'e", 'phlegeth', "r'luh", 'ron', "s'uhn",
         "sgn'wahl", 'shagg', 'shogg', 'shtunggli', 'shugg', "sll'ha", "stell'bsna", "syha'h", 'tharanak', 'throd',
         'uaaah', "uh'e", 'uln', 'vulgtlagln', 'vulgtm', "wgah'n", "y'hah", 'ya', 'zhro']

# I'm confident that we'll find other conjunctions
CONJUNCTIONS = ['mg']

PREFIXES = ['c', "f'", "h'", 'na', 'nafl', 'ng', 'nnn', "ph'", 'y']

SUFFIXES = ['agl', 'nyth', 'og', 'or', 'oth', 'yar']

SENTENCE_ENDS = ['!', '?', '.', '.', '.']
PUNCTUATIONS = SENTENCE_ENDS + [',', ';']


def cthulhu_say(words=10, conjuncionsFreq=.2, prefixesFreq=.25, suffixesFreq=.25, pluralsFreq=.3, punctuationsFreq=.1):
    """Cthulhu says hi!"""
    sentence = [random.choice(WORDS) for x in range(words)]
    for idx in [random.randrange(words) for x in range(int(pluralsFreq * words))]:
        sentence[idx] += sentence[idx][-1]
    for idx in [random.randrange(words) for x in range(int(prefixesFreq * words))]:
        sentence[idx] = random.choice(PREFIXES) + sentence[idx]
    for idx in [random.randrange(words) for x in range(int(suffixesFreq * words))]:
        sentence[idx] += random.choice(SUFFIXES)
    for idx in [random.randrange(1, words - 1) for x in range(int(conjuncionsFreq * words))]:
        sentence[idx] = random.choice(CONJUNCTIONS)
    for idx in [random.randrange(1, words - 1) for x in range(int(punctuationsFreq * words))]:
        punctuation = random.choice(PUNCTUATIONS)
        if sentence[idx].endswith(tuple(PUNCTUATIONS)) or sentence[idx].lower() in CONJUNCTIONS:
            continue
        sentence[idx] += punctuation
        if punctuation in SENTENCE_ENDS:
            sentence[idx+1] = sentence[idx+1].capitalize()
    if sentence:
        sentence[0] = sentence[0].capitalize()
        if punctuationsFreq:
            sentence[-1] += random.choice(SENTENCE_ENDS)
    return ' '.join(sentence)


if __name__ == '__main__':
    print(cthulhu_say())
