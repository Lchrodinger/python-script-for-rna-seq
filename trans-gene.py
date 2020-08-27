# -*- coding: utf-8 -*-
# trans-gene.py
# @author liu yarong
# @description 根据trans_id从gene_id与trans_id的对应文件中提取相应的gene_id
# @created 2020-07-20T08:23:35.485Z+08:00
# @last-modified 2020-07-20T08:40:38.338Z+08:00
#

import sys
if len(sys.argv) != 4:
    print('/nusage:python3 trans-gene.py gen-trans.list trans.list out.txt\n')
    exit()

with open(sys.argv[1], 'r') as gene2trans:
    cor = {}
    for line in gene2trans:
        line = line.strip()
        trans = line.split('\t')[1]
        cor[trans] = line.split('\t')[0]
gene2trans.close()

out = open(sys.argv[3], 'w')
with open(sys.argv[2], 'r') as trans:
    for row in trans:
        row = row.strip()
        if row in cor:
            out.write(cor[row] + '\t')
            out.write(row + '\n')
out.close()
trans.close()
