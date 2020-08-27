# -*- coding: utf-8 -*-
# trans_len.py
# @author liu yarong
# @description 统计fasta文件中每条序列的长度
# @created 2020-07-18T13:31:34.519Z+08:00
# @last-modified 2020-07-22T08:28:17.691Z+08:00
#

import sys

if len(sys.argv) != 3:
    print('/nusage:python3 trans_len.py genome.fa len.out')
    exit()
lens = open(sys.argv[2], 'w')
with open(sys.argv[1], 'r') as genomefa:
    seq = {}
    l = 0
    for line in genomefa:
        line = line.strip()
        if line.startswith('>'):
            name = line.strip()[1:]
            seq[name] = 0
        else:
            l = len(line.strip())
            seq[name] += l
for k, v in seq.items():
    lens.write(k + '\t')
    lens.write(str(v) + '\n')

genomefa.close()
lens.close()
