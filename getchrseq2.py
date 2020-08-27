# -*- coding: utf-8 -*-
# getchrseq2.py
# @author liu yarong
# @description
# @created 2020-07-13T15:35:30.881Z+08:00
# @last-modified 2020-07-13T15:45:26.803Z+08:00
#
import sys

if len(sys.argv) != 2:
    print('\nusage:\npython3 getchrseq.py <genome.fa>')
    exit()

genome_fa = open(sys.argv[1], 'r')
chrseq = {}
for line in genome_fa:
    line = line.strip()
    if line.startswith('>'):
        chrna = line.strip('\n').split('>')[1]
        file = chrna + '.txt'
        seq = open(file, 'w')
        seq.write('>' + chrna + '\n')
    else:
        line = line.strip('\n')
        seq.write(line + '\n')

genome_fa.close()
seq.close()
