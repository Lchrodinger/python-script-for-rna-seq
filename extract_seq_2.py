# -*- coding: utf-8 -*-
# extract_seq_2.py
# @author liu yarong
# @description 根据转录本ID，批量从序列文件中提取目标转录本的序列
# @created 2020-07-14T07:34:44.734Z+08:00
# @last-modified 2020-07-15T21:30:05.810Z+08:00
#

import sys

if len(sys.argv) != 4:
    print(
        '\nusage:python3 extract_seq_2.py<genome_seq.fa><gene_list><seq.fas>')
    exit()

genome_fa = open(sys.argv[1], 'r')
genome_seqs = {}
for line in genome_fa:
    line = line.strip()
    if line.startswith('>'):
        name = line.strip()
        genome_seqs[name] = ''
    else:
        genome_seqs[name] += line.strip()

genome_fa.close()

gene_li = open(sys.argv[2], 'r')
seq_fa = open(sys.argv[3], 'w')
for row in gene_li:
    row = row.strip()
    for key in genome_seqs:
        key = key.split()[0][1:]
        if row == key:
            seq_fa.write('>' + row + '\n')
            seq_fa.write(genome_seqs[row] + '\n')
        else:
            continue
gene_li.close()
seq_fa.close()
