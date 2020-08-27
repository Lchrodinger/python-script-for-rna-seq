# -*- coding: utf-8 -*-
# extract_ss.py
# @author liu yarong
# @description
# @created 2020-07-15T20:08:04.806Z+08:00
# @last-modified 2020-07-15T21:29:20.692Z+08:00
#

import sys
if len(sys.argv) != 3:
    print('\nusage:python3 extract_ss.py fasta.file ss.txt')

with open(sys.argv[1], 'r') as fasta:
    ss = {}
    for line in fasta:
        line = line.strip()
        if line.startswith('>'):
            name = line.strip()
            ss[name] = ''
        else:
            ss[name] += line.strip()
fasta.close()
sa = open(sys.argv[2], 'w')
for k, i in ss.items():
    n = i[:2]
    m = i[-2:]
    sa.write(k + '\n')
    sa.write(n + '\t' + m + '\n')
sa.close()
