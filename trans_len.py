# -*- coding: utf-8 -*-
# trans_len.py
# @author liu yarong
# @description
# @created 2020-07-18T13:31:34.519Z+08:00
# @last-modified 2020-07-22T08:28:55.780Z+08:00
#

import sys

if len(sys.argv) != 4:
    print('/nusage:python3 trans_len.py genome.fa trans.list len.out')
    exit()

with open(sys.argv[1], 'r') as genomefa:
    seq = {}
    l = 0
    for line in genomefa:
        line = line.strip()
        if line.startswith('>'):
            name = line.strip().split(' ')[0][1:]
            seq[name] = 0
        else:
            l = len(line.strip())
            seq[name] += l
genomefa.close()

lens = open(sys.argv[3], 'w')
with open(sys.argv[2], 'r') as trans:
    for row in trans:
        row = row.strip()
        for k, v in seq.items():
            if row == k:
                lens.write(row + '\t')
                lens.write(str(v) + '\n')
                break
            else:
                continue
lens.close()
trans.close()
