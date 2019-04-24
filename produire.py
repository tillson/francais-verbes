#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

verbes = open('verbes').read().split('\n')

tenses = ['present', 'passé composé', 'imparfait', 'subjunctif', 'conditionel', 'futur simple']

print '(Tapes \'q\' sortir)'
cmd = raw_input()

while cmd is not 'q':
    print random.choice(verbes)
    print random.choice(tenses)
    cmd = raw_input()

print 'Adieu!'