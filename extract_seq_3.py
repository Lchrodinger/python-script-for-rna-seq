# -*- coding: utf-8 -*-
# extract_seq_3.py
# @author liu yarong
# @description 根据基因ID从序列文件中提取所有转录本的序列
# @created 2020-08-16T14:51:21.177Z+08:00
# @last-modified 2020-08-22T19:25:57.774Z+08:00
#

import sys

if len(sys.argv) != 4:
    print("\nusage: python3 extract_seq_3.py genome.fa geneid.txt outseq.fa\n")
    exit()

with open(sys.argv[1], 'r') as genomefa:
    seq = {}
    for line in genomefa:
        line = line.strip()
        if line.startswith('>'):
            key = line.strip()[1:]
            seq[key] = ''
        else:
            seq[key] += line.strip()
genomefa.close()

geneid = open(sys.argv[2], 'r')
out = open(sys.argv[3], 'w')
for i in geneid:
    i = i.strip()
    for k in seq:
        m = k.strip().split('=')[1]
        n = k.strip().split(' ')[0]
        if i == m:
            out.write('>' + i + '\t' + n + '\n')
            out.write(seq[k] + '\n')
geneid.close()
out.close()
