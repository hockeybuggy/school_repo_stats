#!/usr/bin/env python

import json
import re

word_count = {}
def count_words(string):
    words = string.split(" ")
    for w in words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1

with open("log.json") as r:
    git_log = json.loads(r.read())

for commit in git_log:
    #print commit["message"]
    count_words(commit["message"])

ordered_wc = sorted(word_count, key=word_count.get, reverse=True)

for i, x in enumerate(ordered_wc):
    print i, "\t", x, "\t", word_count[x]
